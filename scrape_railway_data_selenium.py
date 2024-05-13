from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
import os


# URL of the webpage containing the table
#2024
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2995'

#2023
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2823'

#2022
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2658'

#2021
# url = 'https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,1,304,366,537,1953,2543'

#2020
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2314'


#2019
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2166'

#2018
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2791'

#2016
url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2792'



chrome_options = Options()
prefs = {
    "profile.managed_default_content_settings.images": 2, 
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)
driver.get(url)
time.sleep(3)

# locate the table using xpath
#2024
# table = driver.find_element(By.XPATH, "//*[@id='ntext']/table") 

#2019
table = driver.find_element(By.XPATH,"//*[@id='table20']")
rows = table.find_elements(By.TAG_NAME, "tr")
table_data = []
pdf_filenames = {}  # Dictionary to store PDF filenames keyed by an identifiable column value

for row in rows:
    row_data = []
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        row_data.append(cell.text)
        links = cell.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href.endswith(".pdf"):
                filename = href.split("/")[-1]
                # Assuming the first column contains a unique identifier, use it to map PDF filenames
                pdf_filenames[row_data[0]] = filename
    table_data.append(row_data)

# Close the webdriver
driver.quit()

# Specify the path where you want to save the CSV file
csv_file_path = "2016_table_data.csv"

# Write the scraped table data to the CSV file and append PDF filename and type information
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for i, row_data in enumerate(table_data):
        if i == 0:
            # Add headers for PDF_NAME and TYPE
            row_data.extend(["PDF_NAME", "TYPE"])
        else:
            # Map PDF filename to the row using the identifier in the first column
            pdf_name = pdf_filenames.get(row_data[0], "")
            if len(row_data) > 1 and row_data[1] and row_data[1].split():
                # Split the string and take the first two characters of the first word, then convert to upper case
                type_word = row_data[1].split()[0][:2].upper()
                # Now you can safely use type_word for further processing
            else:
                # Skip this iteration if row_data[1] is null or empty
                continue
            row_data.extend([pdf_name, type_word])
        writer.writerow(row_data)

print(f"Data has been saved to '{csv_file_path}'")
# table_data = []
# pdf_filenames = []  # List to store PDF filenames

# rows = table.find_elements(By.TAG_NAME, "tr")

# for row in rows:
#     # For each row, get the cell contents
#     row_data = []
#     cells = row.find_elements(By.TAG_NAME, "td")
#     for cell in cells:
#         row_data.append(cell.text)
#         links = cell.find_elements(By.TAG_NAME, "a")
#         for link in links:
#             href = link.get_attribute("href")
#             if href.endswith(".pdf"):
#                 # Get the filename from the URL
#                 filename = href.split("/")[-1]
#                 pdf_filenames.append(filename)  # Append filename to the list
#     table_data.append(row_data)

# # Specify the path where you want to save the initial CSV file
# csv_file_path = "2023_table_data.csv"

# # Write the scraped table data to an initial CSV file
# with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     for row_data in table_data:
#         writer.writerow(row_data)

# print(f"Initial table data has been saved to '{csv_file_path}'")

# with open(csv_file_path, mode='r+', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     rows = [row for row in reader]
#     for i, row in enumerate(rows):
#         if i == 0:
#             row.append("PDF_NAME")
#             row.append("TYPE")  # Add a new column for file type
#         else:
#             # print(row[1])
#             # Extract the first word from the second column
#             if len(row) > 1 and row[1]:  # Check if row has at least two elements and the second element is not empty
#                 words = row[1].split()
#                 if words:  # Check if there are words after splitting
#                     type_word = words[0][:2].upper()
#                 else:
#                     type_word = ""  # Handle case where there are no words
#             else:
#                 type_word = "" 
#             row.append(pdf_filenames[i - 1])  # Append PDF name
#             row.append(type_word)  # Append file type
#     file.seek(0)
#     writer = csv.writer(file)
#     writer.writerows(rows)


# # Rewrite the CSV file with the new column
# with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     for row in rows:
#         writer.writerow(row)

# print(f"PDF filenames have been appended as a new column to '{csv_file_path}'")

# # Close the webdriver
# driver.quit()