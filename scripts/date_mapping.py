import csv
import sys

def update_csv_with_dates(year):
    """Function to add date of issue into the csv.

    Args:
        year (str): year for which you want to map the date.
    """
    
    # Define paths based on the specified year
    csv_path1 = f'data/form_data/{year}_table_data.csv'
    csv_path2 = f'output/Year_wise_csv/Railway_data_{year}_with_subject.csv'

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
    with open(csv_path2, mode='w', newline='', encoding='utf-8') as csvfile2:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)

    print(f"The CSV file for year {year} has been updated with new dates.")

def main():
    # Check if the year argument is provided
    if len(sys.argv) < 2:
        print("Usage: python get_json_to_text.py <year>")
        sys.exit(1)

    # Get the year from the command line argument
    year = sys.argv[1]

    # Call the function to process JSON files with the specified year
    update_csv_with_dates(year)

if __name__ == "__main__":
    main()
