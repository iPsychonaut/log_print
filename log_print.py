# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 08:53:45 2023

@author: ian.michael.bollinger@gmail.com with the help of ChatGPT 4.0

EXAMPLE USAGE:

    from /path/to/log_print import log_print

    input_file = '/path/to/file.extension'
    file_extension = pathlib.Path(input_file).suffix
    run_log = input_file.replace(file_extension, '.txt')

    log_print(input_message='PASS: MESSAGE', log_file=run_log) PRINTS IN GREEN TO CONSOLE
    log_print(input_message='NOTE: MESSAGE', log_file=run_log) PRINTS IN CYAN TO CONSOLE
    log_print(input_message='ERROR: MESSAGE', log_file=run_log) PRINTS IN RED TO CONSOLE
    log_print(input_message='MESSAGE', log_file=run_log) PRINTS IN WHITE TO CONSOLE

"""
from datetime import datetime
import pathlib
from termcolor import cprint

def log_print(input_message, log_file):
    """
    Logs a message to a file and prints it to the console with appropriate coloring.

    :param input_message: Message to be logged and printed
    :param log_file: Path to the log file
    """
    now = datetime.now()
    message = f'{now:%M:%S} | {input_message}'

    # Determine the print color based on the input_message content
    message_type_dict = {'PASS': ['light_green', 'green'], 'NOTE': ['cyan'], 'ERROR': ['red']}
    print_color = ['white']  # Default color
    for key, value in message_type_dict.items():
        if key.lower() in input_message.lower():
            print_color = value
            break

    # Writing the message to the log file
    with open(log_file, 'a') as file:
        print(message, file=file)

    # Handling different message types for colored printing
    try:
        cprint(message, print_color[0])
    except (KeyError, IndexError):
        cprint(message, print_color[1] if len(print_color) > 1 else 'white')

# Debuging Main Space & Example
if __name__ == '__main__':
    input_file = 'E:/Entheome_ONT-Illumina_Hybrid_Assembly_Pipeline/test.fastq'
    file_extension = pathlib.Path(input_file).suffix
    run_log = input_file.replace(file_extension, '.txt')

    log_print(input_message='PASS: TEST', log_file=run_log)
    log_print(input_message='NOTE: TEST', log_file=run_log)
    log_print(input_message='ERROR: TEST', log_file=run_log)