# import json
# import pandas as pd

# with open('results/test_jsons/218.pdf.json', 'r') as file:
#     json_data = json.load(file)

# # json_data = json.loads(data)

# # Placeholder for parsed rows
# all_tables = []

# # Iterate through each table in the JSON data
# for table in json_data['analyzeResult']['tables']:
#     # Create a dictionary to hold the data for this table
#     table_data = {}
    
#     # Fill the dictionary with placeholders for each cell
#     for cell in table['cells']:
#         table_data[(cell['rowIndex'], cell['columnIndex'])] = cell['content']
    
#     # Convert the dictionary into a DataFrame
#     # First, collect items into rows based on their rowIndex
#     max_row = max(key[0] for key in table_data.keys()) + 1
#     max_col = max(key[1] for key in table_data.keys()) + 1
    
#     # Prepare rows
#     rows = []
#     for i in range(max_row):
#         row = []
#         for j in range(max_col):
#             row.append(table_data.get((i, j), ""))  # Fill empty cells with an empty string
#         rows.append(row)
    
#     # Create DataFrame and append to list
#     table_df = pd.DataFrame(rows)
#     all_tables.append(table_df)

# # Concatenate all tables if there are more than one table
# final_df = pd.concat(all_tables, ignore_index=True)

# # Save to CSV
# final_df.to_csv('output_tables.csv', index=False)

# print("CSV file has been created with the table data.")




# def read_json_and_extract_content(file_path):
#     # Reading the JSON file
#     with open(file_path, 'r') as file:
#         data = json.load(file)

#     # Extracting "content" fields from the JSON data
#     # contents = []
#     contents = ""
#     for page in data['analyzeResult']['pages']:
#         for word in page['words']:
#             # contents.append(word['content'])
#             contents += word['content'] + " "
            
#     return contents

# text = read_json_and_extract_content('results/test_jsons/218.pdf.json')
# print(text)



# if data.tables:
#     for table_idx, table in enumerate(data.tables):
#         print(f"Table # {table_idx} has {table.row_count} rows and " f"{table.column_count} columns")
#         if table.bounding_regions:
#             for region in table.bounding_regions:
#                 print(f"Table # {table_idx} location on page: {region.page_number} is {region.polygon}")
#         for cell in table.cells:
#             print(f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'")
#             if cell.bounding_regions:
#                 for region in cell.bounding_regions:
#                     print(f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'")

# print("----------------------------------------")







#clean data code
data = """b'THE GENERAL MANAGERs (OPTG.)'
b'COPY TO: CPTMs'
b'ALL ZONAL RAILWAYS'
b'ALL ZONAL RAILWAYS'
b'SL'
b'TRAIN NO. AND NAME'
b'STATION'
b'W.E.F.'
b'1'
b'19165/19166 AHMEDABAD- DARBHANGA SABARMATI EXPRESS'
b'AIT'
b'EARLY CONVENIENT DATE'
b'2'
b'19167/19168 AHMEDABAD- VARANASI CITY SABARMATI EXPRESS'
b'AIT'
b'EARLY CONVENIENT DATE'
b'3'
b'22537/22538 GORAKHPUR- LOKMANYA TILAK (T) EXPRESS'
b'AIT'
b'EARLY CONVENIENT DATE'
b'4'
b'02563/02564 BARAUNI-NEW DELHI SPECIAL EXPRESS'
b'BASTI'
b'EARLY CONVENIENT DATE'
b'5'
b'02569/02570 DARBHANGA-NEW DELHI SPECIAL EXPRESS'
b'BASTI'
b'EARLY CONVENIENT DATE'
b'6'
b'15023/15024 GORAKHPUR- YESVANTPUR EXPRESS'
b'BASTI'
b'EARLY CONVENIENT DATE'
b'7'
b'15903/15904 DIBRUGARH- CHANDIGARH EXPRESS'
b'BASTI'
b'EARLY CONVENIENT DATE'
b'8'
b'19053/19054 SURAT-MUZAFFARPUR EXPRESS'
b'DHAULPUR'
b'EARLY CONVENIENT DATE'
b'9'
b'22539/22540 MAU-ANAND VIHAR (T) EXPRESS'
b'DULLHAPUR'
b'EARLY CONVENIENT DATE'
b'10'
b'15273/15274 RAXAUL-ANAND VIHAR (T) SATYAGRAHA EXPRESS'
b'GAUR'
b'EARLY CONVENIENT DATE'
b'11'
b'12403/12404 PRAYAGRAJ-BIKANER EXPRESS'
b'JHINJHAK'
b'EARLY CONVENIENT DATE'
b'12'
b'12319/12320 KOLKATA-GWALIOR EXPRESS'
b'KANNAUJ'
b'EARLY CONVENIENT DATE'
b'13'
b'19165/19166 AHMEDABAD- DARBHANGA SABARMATI EXPRESS'
b'MOTH'
b'EARLY CONVENIENT DATE'
b'14'
b'19167/19168 AHMEDABAD- VARANASI CITY SABARMATI EXPRESS'
b'MOTH'
b'EARLY CONVENIENT DATE'
b'15'
b'12593/12594 LUCKNOW-BHOPAL EXPRESS'
b'ORAI'
b'EARLY CONVENIENT DATE'
b'16'
b'22467/22468 VARANASI- GANDHINAGAR CAPITAL EXPRESS'
b'ORAI'
b'EARLY CONVENIENT DATE'
b'17'
b'18101/18102 TATANAGAR-JAMMU TAWI EXPRESS'
b'RURA'
b'EARLY CONVENIENT DATE'
b'18'
b'18309/18310 SAMBALPUR-JAMMU TAWI EXPRESS'
b'RURA'
b'EARLY CONVENIENT DATE'
b'19'
b'20403/20404 PRAYAGRAJ-BIKANER EXPRESS'
b'SIRATHU'
b'EARLY CONVENIENT DATE'
b'20'
b'19107/19108 BHAVNAGAR (T)- MARTYR CAPTAIN TUSHAR MAHAJAN JANMABHOOMI EXPRESS'
b'SULTANPUR LODHI'
b'EARLY CONVENIENT DATE'
b'21'
b'19415/19416 SABARMATI-SHRI MATA VAISHNO DEVI KATRA EXPRESS'
b'SULTANPUR LODHI'
b'EARLY CONVENIENT DATE'
b'22'
b'11071 LOKMANYA TILAK (T)-BALLIA KAMAYANI EXPRESS'
b'SURIAWAN'
b'EARLY CONVENIENT DATE'"""
# Split the decoded data into lines
lines = data.split('\n')

# Cleaning each line to remove the "b'" prefix and trailing "'", and prepare for JSON formatting
cleaned_lines = [line.strip("b'").rstrip("'").replace("\\", "\\\\").replace('"', '\\"') for line in lines if line.strip()]

# Joining lines with escaped newline characters for JSON compatibility
json_compatible_string = "\\n".join(cleaned_lines)
print(json_compatible_string)