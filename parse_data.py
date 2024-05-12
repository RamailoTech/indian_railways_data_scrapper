import pandas as pd
import re

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('table_data.csv')

# Define functions to extract information based on subject type
def extract_stoppage_info(subject):
    parts = subject.split(',')
    train_info = parts[0].split(' ')[1:]
    stoppage_station = parts[1].split(' ')[-1]
    return train_info[0], ' '.join(train_info[1:]), stoppage_station

def extract_introduction_info(subject):
    match_intro = re.match(r"Introduction of (.+) (?:between|via) (.+) (?:&|and) (.+)", subject)
    if match_intro:
        train_name = match_intro.group(1)
        start_station = match_intro.group(2)
        end_station = match_intro.group(3)
        return None, train_name, start_station, end_station
    
    return None, None, None


# Apply the functions to extract information and create new columns
def extract_subject_info(row):
    if row['SUBJECT'].startswith('Extension'):
        train_number, train_name, stoppage_station = extract_stoppage_info(row['SUBJECT'])
        return train_number, train_name, stoppage_station, None
    elif row['SUBJECT'].startswith('Introduction'):
        train_number, train_name, start_station, end_station = extract_introduction_info(row['SUBJECT'])
        return train_number, train_name, None, start_station, end_station

# # Apply the function row-wise to extract information
# df[['Train Number', 'Train Name', 'Stoppage Station', 'Start Station', 'End Station']] = df.apply(extract_subject_info, axis=1, result_type='expand')

# # Reorder the columns
# df = df[['CC NO.', 'SUBJECT', 'DATE', 'Train Number', 'Train Name', 'Stoppage Station', 'Start Station', 'End Station']]

# # Write the modified DataFrame back to a CSV file
# df.to_csv('parsed_data.csv', index=False)


def parse_subject(subject):
    match = re.match(r"Stoppage of (\d+/\d+) (.+) at (.+)", subject)
    if match:
        train_number = match.group(1)
        train_name = match.group(2)
        station_name = match.group(3)
        return train_number, train_name, station_name
    else:
        return None, None, None
data = extract_introduction_info('Introduction of new train via Ranchi and Gorakhpur')
print(data)



# import pdfplumber
# import os

# def extract_text_from_pdf(pdf_path):
#     try:
#         with pdfplumber.open(pdf_path) as pdf:
#             text = ""
#             for page in pdf.pages:
#                 text += page.extract_text()
#         return text
#     except Exception as e:
#         print(f"Error occurred while processing {pdf_path}: {e}")
#         return None  

# def count_unparsed_pdfs(folder_path):
#     unparsed_count = 0
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".pdf"):
#             pdf_path = os.path.join(folder_path, filename)
#             text = extract_text_from_pdf(pdf_path)
#             if text is None:
#                 unparsed_count += 1
#     return unparsed_count

# # Example usage
# folder_path = "pdfs/2024_filtered_pdfs"
# unparsed_count = count_unparsed_pdfs(folder_path)
# print(f"Number of unparsed PDFs: {unparsed_count}")
