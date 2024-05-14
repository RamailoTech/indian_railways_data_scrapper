import os
import json
import csv
import re
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import sys

load_dotenv()


def append_text_to_file(filename, text):
    """
    Function to append error message to log file.

    Args:
        filename (str):Name  of the log file
        text (str): Log message.
    """
    with open(filename, 'at') as file:
        file.write(text + "\n")
        
def process_pdfs_for_year(year):
    """
    Process PDF files for a specific year.

    Args:
        year (str): The year for which PDF files will be processed.

    """
    # Configure logging to a file
    log_file_name = f"logs/{year}_parse_pdfs_logs.txt"

    # Azure Form Recognizer credentials and endpoint from environment variables
    key = os.getenv('AZURE_KEY')
    endpoint = os.getenv('AZURE_ENDPOINT')
    document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    # Define the directory path where PDF files are located for the specified year
    directory_path = f"data/pdfs/{year}_filtered_pdfs"

    # Specify the folder path to save JSON files for the parsed data
    output_folder = f"data/parsed_pdfs/parsed_{year}"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the mapping from the CSV file specific to the year
    csv_file_path = f"input/form_data/{year}_table_data.csv"
    type_mapping = {}
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pdf_name = row['PDF_NAME']
            file_type = row['TYPE']
            cc_no = row['CC NO.']
            type_mapping[pdf_name] = (file_type, cc_no)

    #cc no pattern for year 2016 only
    if year == '2016':
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
                file_type, cc_no = type_mapping.get(filename, ('Unknown', 'Unknown'))
                if year == '2016':
                    match = re.match(pattern, cc_no)
                    if match:
                        cc_no = match.group(1)  # Extract digits from the CC NO.

                # Construct the output file path with type and count
                if year != '2016':
                    output_filename = f"Parsed_{file_type}_{year}_{cc_no}.json"
                output_filename = f"Parsed_{file_type}_{year}_{cc_no}_{count}.json"
                output_file_path = os.path.join(output_folder, output_filename)
                count += 1

                # Save the results to a JSON file in the output folder
                with open(output_file_path, "w") as f:
                    json.dump(result_dict, f, indent=4)

                # print(f"Processed {filename} and saved results to {output_file_path}")

            except Exception as e:
                append_text_to_file(log_file_name, f"Error processing {filename}: {str(e)}\n")
                continue  # Skip to the next file

        else:
            append_text_to_file(log_file_name, f"Skipping {filename}, not a PDF.\n")

def main():
    # Check if the year argument is provided
    if len(sys.argv) < 2:
        print("Usage: python get_json_to_text.py <year>")
        sys.exit(1)

    # Get the year from the command line argument
    year = sys.argv[1]

    # Call the function to process JSON files with the specified year
    process_pdfs_for_year(year)

if __name__ == "__main__":
    main()
