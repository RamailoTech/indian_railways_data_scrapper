import os
import json
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import csv
from dotenv import load_dotenv

load_dotenv()


key=os.getenv('KEY')
endpoint = os.getenv('ENDPOINT')
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Define the directory path where PDF files are located
directory_path = "pdfs/2024"

# Specify the folder path to save JSON files
output_folder = "results/parsed_2024"


# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)



# Load the mapping from the CSV file
csv_file_path = 'data/2024_table_data.csv'
type_mapping = {}
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming PDF_NAME is the column that contains the filename
        pdf_name = row['PDF_NAME']
        file_type = row['TYPE']
        cc_no = row['CC NO.']
        type_mapping[pdf_name] = (file_type, cc_no)



for filename in os.listdir(directory_path):
    if filename.endswith("198A.pdf"): 
        document_path = os.path.join(directory_path, filename)
        # print(document_path)
        try:
            # Open and process the PDF file
            with open(document_path, "rb") as document:
                poller = document_analysis_client.begin_analyze_document("prebuilt-layout", document)
                result = poller.result()
                result_dict = result.to_dict()
                
                
                for table_idx, table in enumerate(result.tables):
                    for cell in table.cells:
                        print(cell.content.encode("utf-8"))
                      
                        # lines = data.split('\n')

                        # # Cleaning each line to remove the "b'" prefix and trailing "'"
                        # cleaned_lines = [line.strip("b'").rstrip("'") for line in lines if line.strip()]

                        # # Optionally, print the results to verify
                        # for line in cleaned_lines:
                        #     print(line)
                        # )

          



            # print(f"Processed {filename} and saved results to {output_file_path}")
        
        except Exception as e:
            # append_text_to_file(log_file_name, f"Error processing {filename}: {str(e)}\n")
            continue  # Skip to the next file
        
    else:
        # append_text_to_file(log_file_name, f"Skipping {filename}, not a PDF.\n")
        pass

