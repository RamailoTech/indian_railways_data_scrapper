from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
import sys

def scrape_indian_railways_table(year):
    # Define the base URL with placeholders for the year-specific section ID
    base_url = 'https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,1,304,366,537,1953,{section_id}'

    # Map the year to the corresponding section ID
    year_to_section_id = {
        2016: 2792,
        2018: 2791,
        2019: 2166,
        2020: 2314,
        2021: 2543,
        2022: 2658,
        2023: 2823,
        2024: 2795  
    }

    # Get the section ID for the given year
    section_id = year_to_section_id.get(year)
    if not section_id:
        print(f"Section ID not found for year {year}. Please update the mapping.")
        return

    # Construct the URL for the specified year
    url = base_url.format(section_id=section_id)

    # Configure Chrome options to disable images
    chrome_options = Options()
    prefs = {
        "profile.managed_default_content_settings.images": 2,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    time.sleep(3)

    try:
        # Locate the table using XPath
        table = driver.find_element(By.XPATH,"//*[@id='table20']") # Update XPath based on specific year

        # Extract table data
        rows = table.find_elements(By.TAG_NAME, "tr")
        table_data = []
        pdf_filenames = {}

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
                        pdf_filenames[row_data[0]] = filename
            if row_data:  # Only add non-empty rows to table_data
                table_data.append(row_data)

        # Close the webdriver
        driver.quit()

        # Specify the path where you want to save the CSV file
        csv_file_path = f"data/form_data/{year}_table_data.csv"

        # Write the scraped table data to the CSV file
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Train number', 'Train name', 'Start Station name', 'End Station name', 'Stoppage Station name', 'PDF_NAME', 'TYPE'])

            for row_data in table_data:
                if len(row_data) > 1 and row_data[1] and row_data[1].split():
                    pdf_name = pdf_filenames.get(row_data[0], "")
                    type_word = row_data[1].split()[0][:2].upper()
                    row_data.extend([pdf_name, type_word])
                    writer.writerow(row_data)

        print(f"Data has been saved to '{csv_file_path}'")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        driver.quit()

def main():
    # Check if the year argument is provided
    if len(sys.argv) < 2:
        print("Usage: python scrape_railways_table.py <year>")
        sys.exit(1)

    # Get the year from the command line argument
    year = int(sys.argv[1])  # Convert the year argument to an integer

    # Call the function to scrape Indian Railways table for the specified year
    scrape_indian_railways_table(year)

if __name__ == "__main__":
    main()
