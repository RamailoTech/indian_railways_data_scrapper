import csv

# Paths to your CSV files
csv_path1 = 'data/2024_table_data.csv'  
csv_path2 = 'results/Year_wise_csv/Railway_data_2024_with_subject.csv' 

# Load DATE from the first CSV into a dictionary using CC No. as the key
dates = {}
with open(csv_path1, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cc_no = row['CC NO.']
        dates[cc_no] = row['DATE']

# Read the second CSV and update Date of Issue from the dates dictionary
updated_data = []
with open(csv_path2, mode='r', newline='', encoding='utf-8') as csvfile2:
    reader = csv.DictReader(csvfile2)
    for row in reader:
        cc_no = row['CC No.']
        # Update the Date of Issue if there is a matching CC No. with a new date
        if cc_no in dates:
            row['Date of Issue'] = dates[cc_no]
        updated_data.append(row)

# Write the updated data back to the second CSV file or to a new file
with open(csv_path2, mode='w', newline='', encoding='utf-8') as csvfile2:  # Overwrite the second CSV file
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_data)

print("The second CSV file has been updated with new dates.")