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


# Output directory for PDFs
output_directory = "pdfs"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Run wget command to download PDFs
subprocess.run(["wget", "--no-check-certificate", "-r", "-nd", "-P", output_directory, "-A", "pdf", url])

