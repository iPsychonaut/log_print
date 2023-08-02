# Log Printing Utility

This utility provides functions to log messages to a file and print them to the console with appropriate coloring. It supports different message types and offers flexibility in handling log files.

## Features

- **Colored Console Printing**: Prints messages in different colors based on the message type (e.g., PASS, NOTE, ERROR).
- **Log File Management**: Generates or clears a log file. Can create new files with numerical suffixes if the file already exists.
- **Cross-platform Support**: Handles file paths for different environments such as Windows, Linux, WSL, and Mac.

## Requirements

- Python 3.x
- `termcolor` library

## Installation

Make sure to install the `termcolor` library using the following command:

\```bash
pip install termcolor
\```

## Functions

### `generate_log_file(log_file_path, use_numerical_suffix=False)`

Generates or clears a log file.

- **log_file_path**: Path to the log file.
- **use_numerical_suffix**: If True, creates new files with numerical suffixes if the file exists; otherwise, clears the existing file.

### `log_print(input_message, log_file)`

Logs a message to a file and prints it to the console.

- **input_message**: Message to be logged and printed.
- **log_file**: Path to the log file.

## Usage

Here's how to use the functions:

\```python
input_file = 'E:/Entheome_ONT-Illumina_Hybrid_Assembly_Pipeline/test.fastq'
file_extension = pathlib.Path(input_file).suffix
run_log = input_file.replace(file_extension, '.txt')

# Generate or clear the log file
run_log = generate_log_file(run_log, use_numerical_suffix=False)

log_print(input_message='PASS: TEST', log_file=run_log)
log_print(input_message='NOTE: TEST', log_file=run_log)
log_print(input_message='ERROR: TEST', log_file=run_log)
\```

## Author

Created by ian.michael.bollinger@gmail.com with the help of ChatGPT 4.0 on Wed Aug 2 08:53:45 2023.
