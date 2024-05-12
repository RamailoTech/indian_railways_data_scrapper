from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import ssl
import subprocess

# URL of the webpage containing the table
url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2995'

# Set up Chrome webdriver
chrome_options = Options()
prefs = {
    "profile.managed_default_content_settings.images": 2,
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

# Navigate to the webpage
driver.get(url)
time.sleep(3)

# Locate the table using XPath
table = driver.find_element(By.XPATH, "//*[@id='ntext']/table")

# Find all rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")


# Retry Strategy for handling SSL errors
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)

# HTTP session with the custom adapter
adapter = HTTPAdapter(max_retries=retry_strategy)

# Set SSL version to TLSv1.2
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
adapter.ssl_version = ssl_context

session = requests.Session()
session.mount("https://", adapter)

# Loop through each row to find and download the PDFs
for row in rows:
    # Find all cells in the row
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        # Find links in the cell
        links = cell.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href.endswith(".pdf"):
                # Get the filename from the URL
                filename = os.path.join("pdfs", href.split("/")[-1])
                # Download the PDF
                try:
                    with session.get(href, stream=True) as response:
                        response.raise_for_status()
                        with open(filename, "wb") as f:
                            for chunk in response.iter_content(chunk_size=8192):
                                f.write(chunk)
                except Exception as e:
                    print(f"Failed to download {href}: {e}")

# Close the webdriver
driver.quit()




# # from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # import time
# # import os
# # import requests


# # # URL of the webpage containing the table
# # url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2995'

# # # Set up Chrome webdriver
# # chrome_options = Options()
# # prefs = {
# #     "profile.managed_default_content_settings.images": 2,
# # }
# # chrome_options.add_experimental_option("prefs", prefs)
# # driver = webdriver.Chrome(
# #     service=Service(ChromeDriverManager().install()), options=chrome_options
# # )

# # # Navigate to the webpage
# # driver.get(url)
# # time.sleep(3)

# # # Locate the table using XPath
# # table = driver.find_element(By.XPATH, "//*[@id='ntext']/table")

# # # Find all rows in the table
# # rows = table.find_elements(By.TAG_NAME, "tr")

# # # Create a directory to save the PDFs
# # if not os.path.exists("pdfs"):
# #     os.makedirs("pdfs")

# # # Loop through each row to find and download the PDFs
# # for row in rows:
# #     # Find all cells in the row
# #     cells = row.find_elements(By.TAG_NAME, "td")
# #     for cell in cells:
# #         # Find links in the cell
# #         links = cell.find_elements(By.TAG_NAME, "a")
# #         for link in links:
# #             href = link.get_attribute("href")
# #             if href.endswith(".pdf"):
# #                 # Get the filename from the URL
# #                 filename = os.path.join("pdfs", href.split("/")[-1])
# #                 # Download the PDF
# #                 response = requests.get(href)
# #                 with open(filename, "wb") as f:
# #                     f.write(response.content)

# # # Close the webdriver
# # driver.quit()
