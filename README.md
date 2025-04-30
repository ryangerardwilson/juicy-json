# JuicyJSON

JuicyJSON is a command-line tool for parsing, viewing, and editing JSON files using `jq` and Vim. It provides an interactive interface for navigating JSON structures with dot-notated paths, autocompletion, and the ability to edit JSON directly in Vim, with pretty-printed output for easy readability.

- **Author**: Ryan Gerard Wilson
- **Website**: ryangerardwilson.com

## 1. Installation

To install JuicyJSON, add the APT repository and install the package using the following command:

    bash -c "sh <(curl -fsSL https://files.ryangerardwilson.com/juicyjson/install.sh)"

After installation, the `juicyjson` command is available system-wide.

## 2. Get Latest Version

    sudo apt update
    sudo apt install --only-upgrade juicyjson

## 3. Features

- **Load and Display JSON**: Input JSON via Vim and display it with `jq`'s colorized, pretty-printed output.
- **Interactive Navigation**: Navigate nested JSON structures using dot-notated paths (e.g., `key1.key2.key3`) to focus on specific values.
- **Autocompletion**: Provides real-time autocompletion for JSON keys and array indices as you type paths.
- **Vim Integration**: Edit JSON directly in Vim by typing `vi` during navigation, with changes reflected immediately.
- **User-Friendly Interface**: Features a loading animation, ASCII art logo with typewriter effect, and color-coded output (errors in red, JSON data in blue, instructions in green).
- **Error Handling**: Validates JSON input and provides clear error messages for invalid JSON or `jq` filter errors.
- **Temporary File Management**: Safely handles temporary files for Vim input, ensuring cleanup after use.

## 4. Usage

Run the tool from the command line using:

    juicyjson

The application will:
1. Open Vim for you to input or paste JSON.
2. Display the JSON with `jq`'s colorized formatting.
3. Enter an interactive mode for navigating and editing the JSON.

## 5. Interactive Mode

- **Navigate JSON**: Enter a dot-notated path (e.g., `company.employees.0.name`) to display the corresponding value. Press `Tab` for autocompletion of keys and indices.
- **Edit JSON**: Type `vi` to reopen the JSON in Vim for editing. Save and exit to update the JSON and continue navigation.
- **Exit**: Type `exit` or press `Ctrl+C` to quit.
- **View Full JSON**: Press `Enter` without a path to display the entire JSON.

## 6. Example Workflow

- Start the application:

    juicyjson

- In Vim, paste or write a JSON object, save, and exit (e.g., `:wq`).

    {
      "company": {
        "name": "TechCorp",
        "employees": [
          {"id": 1, "name": "Alice"},
          {"id": 2, "name": "Bob"}
        ]
      }
    }

- View the full JSON (press `Enter`):

    {
      "company": {
        "name": "TechCorp",
        "employees": [
          {"id": 1, "name": "Alice"},
          {"id": 2, "name": "Bob"}
        ]
      }
    }

- Navigate to a specific value:

    Path: company.employees.0.name

    Output:
    "Alice"

- Edit the JSON:

    Path: vi

In Vim, change `"Alice"` to `"Alice Smith"` (or replace with another json to explore), save, and exit. The updated JSON is displayed, and navigation continues.

- Exit the application:

    Path: exit

## 7. License

This project is licensed under the MIT License. See the LICENSE file for details.
