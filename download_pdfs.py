import os
import subprocess

# URL of the webpage containing the table
#2024
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2995'

#2019
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2166'

#2023
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2823'

#2022
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2658'

#2021
# url = 'https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,1,304,366,537,1953,2543'

#2018
# url = 'https://indianrailways.gov.in/rdata/2021_table_data.csvailwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2791'

#2020
# url = 'https://indianrailways.gov.in/railwayboard//view_section.jsp?lang=0&id=0,1,304,366,537,1953,2314'


# Output directory for PDFs
output_directory = "pdfs/2020"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Run wget command to download PDFs
subprocess.run(["wget", "--no-check-certificate", "-r", "-nd", "-P", output_directory, "-A", "pdf", url])
