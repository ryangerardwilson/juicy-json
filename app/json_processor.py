import json
import subprocess
from prompt_toolkit import PromptSession
from json_completer import JSONPathCompleter

class JSONProcessor:
    def pretty_print_json(self, json_str, jq_filter='.'):
        """Process JSON string with jq and return colored output."""
        try:
            json.loads(json_str)  # Validate JSON
            process = subprocess.run(
                ['jq', '--color-output', jq_filter],
                input=json_str,
                text=True,
                capture_output=True,
                check=True
            )
            return process.stdout
        except json.JSONDecodeError as e:
            return f"Error: Invalid JSON - {e}\nInput: {json_str}"
        except subprocess.CalledProcessError as e:
            return f"Error: jq failed - {e.stderr}"
        except Exception as e:
            return f"Error: {str(e)}"

    def interactive_json_navigation(self, json_string, ui, file_handler):
        """Handle interactive JSON navigation with prompt and Vim editing."""
        try:
            json_data = json.loads(json_string)
        except json.JSONDecodeError:
            ui.print_colored("Error: Invalid JSON provided", "red")
            return

        completer = JSONPathCompleter(json_data)
        session = PromptSession(
            "Path: ",
            completer=completer,
            complete_while_typing=True,
            complete_in_thread=True
        )

        ui.print_colored(
            "\nEnter a dot-notated path (e.g., key1.key2.key3) to focus on nested values.\n"
            "Type 'vi' to edit the JSON in Vim, or 'exit' to quit.\n",
            "blue"
        )

        while True:
            try:
                path = session.prompt().strip()
            except KeyboardInterrupt:
                ui.print_colored("\nExiting...", "blue")
                break

            if path.lower() == 'exit':
                break
            elif path.lower() == 'vi':
                new_json = file_handler.open_vim_for_input(json_string)
                if new_json:
                    json_string = new_json
                    try:
                        json_data = json.loads(json_string)
                        completer.json_data = json_data
                        ui.print_colored("\nUpdated JSON:", "blue")
                        ui.print_colored(self.pretty_print_json(json_string), "blue")
                        ui.print_colored(
                            "\nEnter a dot-notated path, 'vi' to edit again, or 'exit' to quit.\n",
                            "blue"
                        )
                    except json.JSONDecodeError:
                        ui.print_colored("\nError: Invalid JSON provided after edit", "red")
                        break
                else:
                    ui.print_colored("\nNo changes made to JSON.", "blue")
                continue

            jq_filter = '.' if not path else f'.{path}'
            result = self.pretty_print_json(json_string, jq_filter)
            ui.print_colored(result, "blue")
