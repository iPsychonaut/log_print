# Log Print Utility

A simple Python utility that logs a message to a file and prints it to the console with appropriate coloring based on the message type.

## Requirements

- Python 3.x
- `termcolor` library

## Installation

Make sure to install the `termcolor` library using the following command:

\```bash
pip install termcolor
\```

## Usage

To use this utility, simply import the `log_print` function and call it with the appropriate parameters.

\```python
from /path/to/log_print import log_print

input_file = '/path/to/file.extension'
file_extension = pathlib.Path(input_file).suffix
run_log = input_file.replace(file_extension, '.txt')

log_print(input_message='PASS: MESSAGE', log_file=run_log)  # PRINTS IN GREEN TO CONSOLE
log_print(input_message='NOTE: MESSAGE', log_file=run_log)  # PRINTS IN CYAN TO CONSOLE
log_print(input_message='ERROR: MESSAGE', log_file=run_log) # PRINTS IN RED TO CONSOLE
log_print(input_message='MESSAGE', log_file=run_log)        # PRINTS IN WHITE TO CONSOLE
\```

## Message Types

- **PASS**: Prints in green
- **NOTE**: Prints in cyan
- **ERROR**: Prints in red
- No specific type: Prints in white

## Author

Created by ian.michael.bollinger@gmail.com with the help of ChatGPT 4.0 on Wed Aug 2 08:53:45 2023
