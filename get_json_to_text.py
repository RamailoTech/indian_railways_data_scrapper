import json
import pandas as pd
import os
import re



log_file_name = "logs/2024_json_to_text.txt"
# Configure logging to a file
def append_text_to_file(filename, text):
    # Open the file in append mode ('a') and text mode ('t'), hence 'at'
    with open(filename, 'at') as file:
        # Write the text followed by a newline character
        file.write(text + "\n")
        
# Define the directory containing the JSON files
json_dir = 'results/parsed_2016'
output_dir = 'results/json_to_txt/2016'

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)


# Iterate over each file in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        
        # Use regex to define the output filename from the input filename
        # match = re.match(r'Parsed_([A-Z]+)_2016_(\d+)\.json', filename)
        match = re.match(r'Parsed_([A-Z]+)_2016_(\d+)_(\d+)\.json',filename)
        if match:
            file_type = match.group(1)
            file_number = match.group(2)
            count = match.group(3)
            output_filename = f"{file_type}_{file_number}_{count}.txt"
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
                for paragraph in json_data.get('paragraphs', []):  # Use .get to avoid KeyError if 'paragraphs' is not found
                    content = paragraph['content']
                    if len(content.split()) > 20:  # Checking for more than 20 words
                        output_file.write(content + '\n\n')

                # Begin tabular data section
                output_file.write("Tabular data:\n\n")

                # Process each table in the JSON file
                for i, table in enumerate(json_data.get('tables', [])):  # Use .get to avoid KeyError if 'tables' is not found
                    table_data = {}
                    header_data = {}

                    # Extract cell data to dictionary, considering both column headers and content cells
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

#todo

# import json
# import pandas as pd
# import os
# import re

# # Define the directory containing the JSON files
# json_dir = 'results/parsed_2024'
# output_dir = 'results/json_to_txt/2024'

# # Make sure output directory exists
# os.makedirs(output_dir, exist_ok=True)

# # Iterate over each file in the directory
# for filename in os.listdir(json_dir):
#     if filename.endswith('.json'):
#         file_path = os.path.join(json_dir, filename)
        
#         # Define the output file path using the input filename
#         match = re.match(r'Parsed_([A-Z]+)_2024_(\d+)\.json', filename)
#         if match:
#             file_type = match.group(1)
#             file_number = match.group(2)
#             output_filename = f"{file_type}_{file_number}.txt"
#         output_file_path = os.path.join(output_dir, output_filename)

#         # Open the output text file for writing
#         with open(output_file_path, 'w') as output_file:

#             # Open and load the JSON file
#             with open(file_path, 'r') as file:
#                 json_data = json.load(file)

#             # Process paragraphs in the JSON file
#             if 'paragraphs' in json_data['analyzeResult']:
#                 for paragraph in json_data['analyzeResult']['paragraphs']:
#                     content = paragraph['content']
#                     if len(content.split()) > 20:  # Checking for more than 15 words
#                         output_file.write(content + '\n\n')

#             # Begin tabular data section
#             output_file.write("Tabular data:\n\n")

#             # Process each table in the JSON file
#             for i, table in enumerate(json_data['analyzeResult']['tables']):
#                 table_data = {}

#                 # Extract cell data to dictionary
#                 for cell in table['cells']:
#                     table_data[(cell['rowIndex'], cell['columnIndex'])] = cell['content']

#                 # Determine maximum row and column indices
#                 max_row = max(key[0] for key in table_data.keys()) + 1
#                 max_col = max(key[1] for key in table_data.keys()) + 1

#                 # Prepare rows for DataFrame
#                 rows = []
#                 for row_index in range(max_row):
#                     row = []
#                     for col_index in range(max_col):
#                         row.append(table_data.get((row_index, col_index), ""))
#                     rows.append(row)

#                 # Create DataFrame from rows
#                 table_df = pd.DataFrame(rows)

#                 # Write table header to text file
#                 output_file.write(f"Table {i+1}:\n")
#                 # Write DataFrame to text file with pipe delimiter
#                 table_df.to_csv(output_file, sep='|', index=False, header=False)
#                 output_file.write('\n')  # Ensure there's a blank line after each table

#         print(f"All data have been successfully written to {output_file_path}")



# #todo