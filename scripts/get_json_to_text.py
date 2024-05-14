import json
import pandas as pd
import os
import re
import sys


def append_text_to_file(filename, text):
    # Open the file in append mode ('a') and text mode ('t'), hence 'at'
    with open(filename, 'at') as file:
        # Write the text followed by a newline character
        file.write(text + "\n")


def process_json_files(year):
    """Function to extract contents (word count greater than 20) and tabular data from parsed json files. This function returns a text file.

    Args:
        year (str): Year for which json is to be converted into text files.
    """
    
    log_file_name = f"logs/{year}_json_to_text.txt"
    if not os.path.exists(log_file_name):
        with open(log_file_name, 'w') as log_file:
            log_file.write(f"Log file for {year} processing\n")
            
    json_dir = f"data/parsed_pdfs/parsed_{year}"
    output_dir = f"data/parsed_text/{year}"

    # Make sure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each file in the directory
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(json_dir, filename)

            # Use regex to define the output filename from the input filename
            match = re.match(rf'Parsed_([A-Z]+)_{year}_(\d+).json', filename)
            if match:
                file_type = match.group(1)
                file_number = match.group(2)
                output_filename = f"{file_type}_{file_number}.txt"
                output_file_path = os.path.join(output_dir, output_filename)
            else:
                continue

            try:
                # Open the output text file for writing
                with open(output_file_path, 'w') as output_file:
                    # Open and load the JSON file
                    with open(file_path, 'r') as file:
                        json_data = json.load(file)

                    # Process paragraphs in the JSON file
                    for paragraph in json_data.get('paragraphs', []):
                        content = paragraph['content']
                        if len(content.split()) > 20:
                            output_file.write(content + '\n\n')

                    # Begin tabular data section
                    output_file.write("Tabular data:\n\n")

                    # Process each table in the JSON file
                    for i, table in enumerate(json_data.get('tables', [])):
                        table_data = {}
                        header_data = {}

                        # Extract cell data to dictionary
                        for cell in table['cells']:
                            if cell['kind'] == "columnHeader":
                                header_data[(cell['row_index'], cell['column_index'])] = cell['content']
                            table_data[(cell['row_index'], cell['column_index'])] = cell['content']

                        # Determine maximum row and column indices
                        max_row = max(key[0] for key in table_data.keys()) + 1
                        max_col = max(key[1] for key in table_data.keys()) + 1

                        # Prepare rows for DataFrame
                        rows = []
                        for row_index in range(max_row):
                            row = []
                            for col_index in range(max_col):
                                row.append(table_data.get((row_index, col_index), ""))
                            rows.append(row)
                           

                        # Create DataFrame from rows
                        table_df = pd.DataFrame(rows)
                        output_file.write(f"Table {i+1}:\n")
                        table_df.to_csv(output_file, sep='|', index=False, header=False)
                        output_file.write('\n')  # Ensure there's a blank line after each table
                print(f"All data have been successfully written to {output_file_path}")
                

            except Exception as e:
                append_text_to_file(log_file_name, f"Error processing {filename}: {str(e)}\n")
                continue

def main():
    # Check if the year argument is provided
    if len(sys.argv) < 2:
        print("Usage: python get_json_to_text.py <year>")
        sys.exit(1)

    # Get the year from the command line argument
    year = sys.argv[1]

    # Call the function to process JSON files with the specified year
    process_json_files(year)

if __name__ == "__main__":
    main()
