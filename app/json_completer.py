from prompt_toolkit.completion import Completer, Completion

class JSONPathCompleter(Completer):
    def __init__(self, json_data):
        self.json_data = json_data

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        parts = text.split('.')
        current_path = parts[:-1]
        partial_key = parts[-1] if parts else ''

        current_node = self.json_data
        for part in current_path:
            if part.isdigit() and isinstance(current_node, list):
                try:
                    current_node = current_node[int(part)]
                except (IndexError, ValueError):
                    return
            elif isinstance(current_node, dict):
                current_node = current_node.get(part, {})
            else:
                return

        if isinstance(current_node, dict):
            for key in current_node.keys():
                if key.startswith(partial_key):
                    yield Completion(key, start_position=-len(partial_key))
        elif isinstance(current_node, list):
            for i in range(len(current_node)):
                if str(i).startswith(partial_key):
                    yield Completion(str(i), start_position=-len(partial_key))
