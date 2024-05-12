from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
import os


# URL of the webpage containing the table
url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2995'


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
table = driver.find_element(By.XPATH, "//*[@id='ntext']/table")

table_data = []
pdf_filenames = []  # List to store PDF filenames

rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    # For each row, get the cell contents
    row_data = []
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        row_data.append(cell.text)
        links = cell.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href.endswith(".pdf"):
                # Get the filename from the URL
                filename = href.split("/")[-1]
                pdf_filenames.append(filename)  # Append filename to the list
    table_data.append(row_data)

# Specify the path where you want to save the initial CSV file
csv_file_path = "table_data.csv"

# Write the scraped table data to an initial CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row_data in table_data:
        writer.writerow(row_data)

print(f"Initial table data has been saved to '{csv_file_path}'")

with open(csv_file_path, mode='r+', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]
    for i, row in enumerate(rows):
        if i == 0:
            row.append("PDF_NAME")
            row.append("TYPE")  # Add a new column for file type
        else:
            # Extract the first word from the second column
            type_word = row[1].split()[0][:2].upper()
            row.append(pdf_filenames[i - 1])  # Append PDF name
            row.append(type_word)  # Append file type
    file.seek(0)
    writer = csv.writer(file)
    writer.writerows(rows)


# Rewrite the CSV file with the new column
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)

print(f"PDF filenames have been appended as a new column to '{csv_file_path}'")

# Close the webdriver
driver.quit()
