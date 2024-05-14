import os
import csv
import openai
import sys
from dotenv import load_dotenv
from encoding_scripts import (
    get_policy_encoding_stoppage_results,
    get_policy_encoding_introduced_results,
    get_policy_encoding_extension_results
)

load_dotenv()
openai.api_key = os.getenv("API_KEY")
openai.api_type = os.getenv("API_TYPE")

def process_year_data(year):
    """Function to process a year's data(processed text file) and extarct train information using LLM. Stores the final output into a csv file.

    Args:
        year (str): Year for which you want to process data.
    """
    # Define paths based on the specified year
    subject_csv_path = f'data/form_data/{year}_table_data.csv'
    directory_path = f'data/parsed_text/{year}'
    output_csv_path = f'output/Year_wise_csv/Railway_data_{year}_with_subject.csv'

    # Load subjects from CSV into a dictionary
    subjects_dict = {}
    with open(subject_csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            subjects_dict[row['CC NO.']] = row['SUBJECT']

    # Write results to CSV
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = [
            'CC No.', 'Type', 'Train number', 'Train name', 
            'Start Station name', 'End Station name', 'Stoppage Station name', 'Date of Issue'
        ]
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
                if file_type == 'stoppage':
                    results = get_policy_encoding_stoppage_results(full_text)
                elif file_type == 'introduction':
                    results = get_policy_encoding_introduced_results(full_text)
                elif file_type == 'extension':
                    results = get_policy_encoding_extension_results(full_text)

                for result in results:
                    row_data = {'CC No.': cc_no, 'Type': file_type}
                    # Fill in each column, use None for missing fields
                    for field in fieldnames[2:]:  # Skip CC No. and Type since they're already set
                        row_data[field] = result.get(field, "")
                    # Write the results to the CSV file
                    writer.writerow(row_data)
                    

    print(f"Results have been written to {output_csv_path}")



def main():
    # Check if the year argument is provided
    if len(sys.argv) < 2:
        print("Usage: python get_json_to_text.py <year>")
        sys.exit(1)

    # Get the year from the command line argument
    year = sys.argv[1]

    # Call the function to process JSON files with the specified year
    process_year_data(year)

if __name__ == "__main__":
    main()