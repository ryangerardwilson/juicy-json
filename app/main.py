import sys
import threading
import time
from ui import UI
from json_processor import JSONProcessor
from file_handler import FileHandler

class App:
    def __init__(self):
        self.ui = UI()
        self.json_processor = JSONProcessor()
        self.file_handler = FileHandler()

    def run(self):
        # Display the logo
        self.ui.display_logo()

        # Run loading animation for 3 seconds
        stop_event = threading.Event()
        animation_thread = threading.Thread(
            target=self.ui.animate_loading,
            args=(stop_event, "Now, dump that ugly-ass json in vim")
        )
        animation_thread.start()
        stop_event.set()
        animation_thread.join()

        # Get JSON input from Vim
        json_string = self.file_handler.open_vim_for_input()
        if not json_string:
            self.ui.print_colored("Error: No input provided", "red")
            sys.exit(1)

        # Display initial JSON
        result = self.json_processor.pretty_print_json(json_string)
        self.ui.print_colored(result, "blue")

        # Start interactive navigation
        self.json_processor.interactive_json_navigation(json_string, self.ui, self.file_handler)

if __name__ == "__main__":
    app = App()
    app.run()
