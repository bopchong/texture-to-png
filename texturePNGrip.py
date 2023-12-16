#!/usr/bin/env python
# coding: utf-8

import os
import base64
import re
import sys

def process_file(input_file_path, folder_path):
    # Read the first line of the input file
    with open(input_file_path, 'r') as input_file:
        first_line = input_file.readline().strip()

    # Extract relevant data from the first line
    data_split = first_line.split(",")
    img_data_str = data_split[2].split("\"")
    img_data = img_data_str[3]

    # Convert from base64 to bytes
    img_data_bytes = base64.b64decode(img_data)

    # Get texture name for file naming
    texture_name_split = re.split(r'\W+', data_split[1])
    texture_name = texture_name_split[2]
    texture_file_name = texture_name + '_texture.png'

    # Construct the output file path
    output_file_path = os.path.join(folder_path, texture_file_name)

    # Write the decoded image data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(img_data_bytes)

def process_folder(folder_path):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.texture')]

    # Process each .texture file in the folder
    for file_name in files:
        input_file_path = os.path.join(folder_path, file_name)
        process_file(input_file_path, folder_path)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    # Get the folder path from the command line arguments
    folder_path = sys.argv[1]

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        sys.exit(1)

    # Process the folder
    process_folder(folder_path)

    print("Processing completed.")
