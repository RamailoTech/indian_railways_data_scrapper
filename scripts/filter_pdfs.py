import csv
import os
import shutil
import sys

def append_text_to_file(filename, text):
    """
    Function to append error message to log file.

    Args:
        filename (str):Name  of the log file
        text (str): Log message.
    """
    if not os.path.exists(filename):
        with open(filename, 'at') as file:
            file.write(text + "\n")

def filter_and_copy_pdfs(year):
    """Function to filter pdfs for type extension, introduction and stoppage only.

    Args:
        year (str): required year
    """
    # Paths based on the specified year
    pdf_folder = f'data/pdfs/{year}'  # Path to the folder containing PDFs for the specified year
    csv_file_path = f'data/form_data/{year}_table_data.csv'  # Path to the CSV file for the specified year
    new_folder = f'data/pdfs/{year}_filtered_pdfs'  # Path to the new folder to save filtered PDFs

    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Filter PDFs based on the specified types
    filtered_pdfs = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['TYPE'] in ['IN', 'ST', 'EX']:  # Add more types as needed
                pdf_name = row['PDF_NAME']
                pdf_path = os.path.join(pdf_folder, pdf_name)
                # if os.path.exists(pdf_path):
                filtered_pdfs.append(pdf_path)
    
    log_file = "logs/filter_pdf_logs.txt"
    # Copy filtered PDFs to the new folder
    for pdf_path in filtered_pdfs:
        try:
            if os.path.isfile(pdf_path):  # Check if the path is a valid file
                shutil.copy(pdf_path, new_folder)
            else:
                append_text_to_file(log_file,f"Skipped (not a file): {pdf_path}")
        except Exception as e:
            append_text_to_file(f"Error copying file: {pdf_path} - {e}")

    print(f"{len(filtered_pdfs)} PDFs filtered and saved to '{new_folder}'.")





def main():
    # Check if the year argument is provided
    if len(sys.argv) < 2:
        print("Usage: python get_json_to_text.py <year>")
        sys.exit(1)

    # Get the year from the command line argument
    year = sys.argv[1]

    # Call the function to process JSON files with the specified year
    filter_and_copy_pdfs(year)

if __name__ == "__main__":
    main()