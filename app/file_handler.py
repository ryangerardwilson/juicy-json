import subprocess
import tempfile
import os

class FileHandler:
    def open_vim_for_input(self, initial_content=None):
        """Open Vim for JSON input and return the content."""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            temp_file_path = temp_file.name
            if initial_content is not None:
                temp_file.write(initial_content.encode('utf-8'))
                temp_file.flush()

        try:
            subprocess.run(['vim', temp_file_path], check=True)
            with open(temp_file_path, 'r') as f:
                json_string = f.read().strip()
            return json_string
        finally:
            os.unlink(temp_file_path)
