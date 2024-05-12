import csv
import os
import shutil

# Paths
pdf_folder = 'pdfs/2024'  # Path to the folder containing PDFs
csv_file_path = 'data/2024_table_data.csv'  # Path to the CSV file
new_folder = 'pdfs/2024_filtered_pdfs'  # Path to the new folder to save filtered PDFs

# Create the new folder if it doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Filter PDFs based on the specified types
filtered_pdfs = []
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['TYPE'] in ['IN', 'ST','EX']:
            pdf_name = row['PDF_NAME']
            pdf_path = os.path.join(pdf_folder, pdf_name)
            if os.path.exists(pdf_path):
                filtered_pdfs.append(pdf_path)

# Copy filtered PDFs to the new folder
for pdf_path in filtered_pdfs:
    shutil.copy(pdf_path, new_folder)

print(f"{len(filtered_pdfs)} PDFs filtered and saved to '{new_folder}'.")
