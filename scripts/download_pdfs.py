import os
import subprocess
import sys

def download_pdfs(url, output_directory):
    """
    Download PDFs from a specified URL to a given output directory.
    
    Args:
        url (str): The URL from which to download PDFs.
        output_directory (str): The directory where downloaded PDFs will be saved.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Run wget command to download PDFs
    subprocess.run(["wget", "--no-check-certificate", "-r", "-nd", "-P", output_directory, "-A", "pdf", url]) 

 
    
def main():
    # Check if the year argument is provided
    if len(sys.argv) < 2:
        print("Usage: python get_json_to_text.py <year>")
        sys.exit(1)

    # Get the year from the command line argument
    year = sys.argv[1]
    output_directory = f"data/pdfs/{year}"
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

    # Construct the URL for the specified year
    url = base_url.format(section_id=section_id)

    # Call the function to process JSON files with the specified year
    download_pdfs(url,output_directory)

if __name__ == "__main__":
    main()