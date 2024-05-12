import os
import openai
import csv
from encoding_scripts import (
    get_policy_encoding_stoppage_results,
    get_policy_encoding_introduced_results,
    get_policy_encoding_extension_results
)
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")
openai.api_type = os.getenv("API_TYPE")

def get_results(extracted_text, type):
    if type == "stoppage":
        encoded_data = get_policy_encoding_stoppage_results(extracted_text)
    elif type == "introduction":
        encoded_data = get_policy_encoding_introduced_results(extracted_text)
    elif type == "extension":
        encoded_data = get_policy_encoding_extension_results(extracted_text)
    return encoded_data

# Load subjects from CSV
subjects_dict = {}
subject_csv_path = 'data/2024_table_data.csv'
with open(subject_csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        subjects_dict[row['CC NO.']] = row['SUBJECT']

# Define the path to the directory containing the files
directory_path = 'results/json_to_txt/2024'
output_csv_path = 'results/Year_wise_csv/Railway_data_2024_with_subject.csv'

# Write results to CSV
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['CC No.', 'Type', 'Train number', 'Train name', 'Start Station name', 'End Station name', 'Stoppage Station name', 'Date of Issue']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            # Extract type and CC No. from filename
            parts = filename.split('_')
            file_type_prefix = parts[0]
            cc_no = parts[-1].split('.')[0]

            # Map prefix to type
            if file_type_prefix == 'ST':
                file_type = 'stoppage'
            elif file_type_prefix == 'EX':
                file_type = 'extension'
            elif file_type_prefix == 'IN':
                file_type = 'introduction'

            # Read the file content
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                extracted_text = file.read()
            # Prepend subject if CC No. matches
            subject = subjects_dict.get(cc_no, "")
            full_text = f"Subject:\n{subject}\n\n{extracted_text}"

            # Get results based on type
            results = get_results(full_text, file_type)

            for result in results:
                row_data = {'CC No.': cc_no, 'Type': file_type}
                # Fill in each column, use None for missing fields
                for field in fieldnames[2:]:  # Skip CC No. and Type since they're already set
                    row_data[field] = result.get(field, "")
                # Write the results to the CSV file
                writer.writerow(row_data)

print(f"Results have been written to {output_csv_path}")



##without subject

# import os 
# import openai
# import json 
# from encoding_scripts import get_policy_encoding_stoppage_results,get_policy_encoding_introduced_results,get_policy_encoding_extension_results
# from dotenv import load_dotenv
# import csv

# load_dotenv()

# openai.api_key = os.getenv("API_KEY")
# openai.api_type = os.getenv("API_TYPE")




# def get_results(extracted_text,type):
#     if type == "stoppage":
#         encoded_data = get_policy_encoding_stoppage_results(extracted_text)
#     elif type == "introduction":
#         encoded_data = get_policy_encoding_introduced_results(extracted_text)
#     elif type == "extension":
#         encoded_data = get_policy_encoding_extension_results(extracted_text)
        
#     return encoded_data


# # Define the path to the directory containing the files
# directory_path = 'results/json_to_txt/2024'
# output_csv_path = 'results/Year_wise_csv/Railway_data_2024_without_subject.csv'


# # Write results to CSV
# with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
#     fieldnames = ['CC No.', 'Type', 'Train number', 'Train name', 'Start Station name', 'End Station name', 'Stoppage Station name', 'Date of Issue']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()

#     # Iterate through files in the directory
#     for filename in os.listdir(directory_path):
#         if filename.endswith(".txt"):
#             # Extract type and CC No. from filename
#             parts = filename.split('_')
#             file_type_prefix = parts[0]
#             cc_no = parts[-1].split('.')[0]

#             # Map prefix to type
#             if file_type_prefix == 'ST':
#                 file_type = 'stoppage'
#             elif file_type_prefix == 'EX':
#                 file_type = 'extension'
#             elif file_type_prefix == 'IN':
#                 file_type = 'introduction'

#             # Read the file content
#             file_path = os.path.join(directory_path, filename)
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 extracted_text = file.read()

#             # Get results based on type
#             results = get_results(extracted_text, file_type)

#             for result in results:
#                 row_data = {
#                     'CC No.': cc_no,
#                     'Type': file_type
#                 }
#                 # Fill in each column, use None for missing fields
#                 for field in fieldnames[2:]:  # Skip CC No. and Type since they're already set
#                     row_data[field] = result.get(field, "")

#                 # Write the results to the CSV file
#                 writer.writerow(row_data)

# print(f"Results have been written to {output_csv_path}")