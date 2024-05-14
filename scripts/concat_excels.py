import pandas as pd
import os

# Directory containing CSV files
directory_path = "output/Year_wise_csv"  # Change this to your CSV directory

# Output Excel file
output_excel_file = "output/Combined_Railway_Data.xlsx"

# Create a Pandas Excel writer using openpyxl as the engine
writer = pd.ExcelWriter(output_excel_file, engine='openpyxl')

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Extract the year from the filename
        year = filename.split('_')[2]  # Assuming the format is 'Railway_data_YYYY_with_subject.csv'

        # Construct full file path
        file_path = os.path.join(directory_path, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Write the data to a new sheet in the Excel file
        df.to_excel(writer, sheet_name=year, index=False)

# Save and close the Excel workbook
writer.close()

print("All CSV files have been successfully written to the Excel workbook.")
