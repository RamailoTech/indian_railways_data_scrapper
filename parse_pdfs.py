import os
import json
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import csv
from dotenv import load_dotenv
import re

load_dotenv()


log_file_name = "logs/2024_parse_pdfs_logs.txt"
# Configure logging to a file
def append_text_to_file(filename, text):
    # Open the file in append mode ('a') and text mode ('t'), hence 'at'
    with open(filename, 'at') as file:
        # Write the text followed by a newline character
        file.write(text + "\n")


key=os.getenv('KEY')
endpoint = os.getenv('ENDPOINT')
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Define the directory path where PDF files are located
directory_path = "pdfs/2016_filtered_pdfs"

# Specify the folder path to save JSON files
output_folder = "results/parsed_2016"


# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)



# Load the mapping from the CSV file
csv_file_path = 'data/2016_table_data.csv'
type_mapping = {}
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming PDF_NAME is the column that contains the filename
        pdf_name = row['PDF_NAME']
        file_type = row['TYPE']
        cc_no = row['CC NO.']
        type_mapping[pdf_name] = (file_type, cc_no)

pattern = r"^[^/]+/[^/]+/([^/]+)"
count = 1
for filename in os.listdir(directory_path):
    if filename.endswith(".pdf"): 
        document_path = os.path.join(directory_path, filename)
        
        try:
            # Open and process the PDF file
            with open(document_path, "rb") as document:
                poller = document_analysis_client.begin_analyze_document("prebuilt-layout", document)
                result = poller.result()
                result_dict = result.to_dict()

                
            # Determine the output file type from the CSV mapping
            file_type, cc_no = type_mapping.get(filename, 'Unknown')
            year="2016"
            match = re.match(pattern, cc_no)
            if match:
                cc_no = match.group(1)  # The first capturing group contains the digits
            # Construct the output file path with type
            
            output_filename = f"Parsed_{file_type}_{year}_{cc_no}_{count}.json"
            output_file_path = os.path.join(output_folder, output_filename)
            count+=1
            # Save the results to a JSON file in the output folder
            with open(output_file_path, "w") as f:
                json.dump(result_dict, f, indent=4)

            print(f"Processed {filename} and saved results to {output_file_path}")
        
        except Exception as e:
            append_text_to_file(log_file_name, f"Error processing {filename}: {str(e)}\n")
            continue  # Skip to the next file
        
    else:
        append_text_to_file(log_file_name, f"Skipping {filename}, not a PDF.\n")

