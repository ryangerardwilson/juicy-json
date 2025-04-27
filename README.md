# JuicyJSON

JuicyJSON is a command-line tool for parsing, viewing, and editing JSON files using `jq` and Vim. It provides an interactive interface for navigating JSON structures with dot-notated paths, autocompletion, and the ability to edit JSON directly in Vim, with pretty-printed output for easy readability.

## Author

- **Name**: Ryan Gerard Wilson
- **Website**: ryangerardwilson.com

## Features

- **Load and Display JSON**: Input JSON via Vim and display it with `jq`'s colorized, pretty-printed output.
- **Interactive Navigation**: Navigate nested JSON structures using dot-notated paths (e.g., `key1.key2.key3`) to focus on specific values.
- **Autocompletion**: Provides real-time autocompletion for JSON keys and array indices as you type paths.
- **Vim Integration**: Edit JSON directly in Vim by typing `vi` during navigation, with changes reflected immediately.
- **User-Friendly Interface**: Features a loading animation, ASCII art logo with typewriter effect, and color-coded output (errors in red, JSON data in blue, instructions in green).
- **Error Handling**: Validates JSON input and provides clear error messages for invalid JSON or `jq` filter errors.
- **Temporary File Management**: Safely handles temporary files for Vim input, ensuring cleanup after use.

## Installation

To install JuicyJSON, add the APT repository and install the package using the following command:

```bash
bash -c "sh <(curl -fsSL https://files.ryangerardwilson.com/juicyjson/install.sh)"
```

This will:
1. Download and install the GPG key for the `juicyjson` repository.
2. Add the `juicyjson` repository to your APT sources list.
3. Update the APT cache and install the `juicyjson` package.

After installation, the `juicyjson` command is available system-wide.

## Usage

Run the tool from the command line using:

```bash
juicyjson
```

The application will:
1. Display an ASCII art logo with a typewriter effect.
2. Show a loading animation for 3 seconds.
3. Open Vim for you to input or paste JSON.
4. Display the JSON with `jq`'s colorized formatting.
5. Enter an interactive mode for navigating and editing the JSON.

### Interactive Mode

- **Navigate JSON**: Enter a dot-notated path (e.g., `company.employees.0.name`) to display the corresponding value. Press `Tab` for autocompletion of keys and indices.
- **Edit JSON**: Type `vi` to reopen the JSON in Vim for editing. Save and exit to update the JSON and continue navigation.
- **Exit**: Type `exit` or press `Ctrl+C` to quit.
- **View Full JSON**: Press `Enter` without a path to display the entire JSON.

### Example Workflow

1. Start the application:

   ```bash
   juicyjson
   ```

2. In Vim, paste or write a JSON object, save, and exit (e.g., `:wq`).

   Example JSON:
   ```json
   {
     "company": {
       "name": "TechCorp",
       "employees": [
         {"id": 1, "name": "Alice"},
         {"id": 2, "name": "Bob"}
       ]
     }
   }
   ```

3. View the full JSON (press `Enter`):

   Output (colorized by `jq`):
   ```json
   {
     "company": {
       "name": "TechCorp",
       "employees": [
         {"id": 1, "name": "Alice"},
         {"id": 2, "name": "Bob"}
       ]
     }
   }
   ```

4. Navigate to a specific value:

   ```
   Path: company.employees.0.name
   ```

   Output:
   ```json
   "Alice"
   ```

5. Edit the JSON:

   ```
   Path: vi
   ```

   In Vim, change `"Alice"` to `"Alice Smith"`, save, and exit. The updated JSON is displayed, and navigation continues.

6. Exit the application:

   ```
   Path: exit
   ```

## Error Handling

- **Invalid JSON**: Displays an error in red if the input JSON is malformed, with details about the parsing error.
- **Invalid Paths**: Shows `jq` error messages for incorrect or nonexistent paths.
- **Vim Errors**: Handles Vim subprocess errors gracefully, ensuring temporary files are cleaned up.
- **Empty Input**: Exits with an error if no JSON is provided after Vim input.
- **Keyboard Interrupt**: Exits cleanly on `Ctrl+C` with a farewell message.

## Notes

- The tool uses threading for the loading animation to keep the CLI responsive.
- Output is color-coded: JSON data and instructions in blue, logo and loading messages in green, errors in red.
- Autocompletion is dynamic, updating with edited JSON after Vim sessions.
- Temporary files are created with a `.json` suffix and deleted after use.
- Requires `jq` for JSON processing and `vim` for input/editing.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
