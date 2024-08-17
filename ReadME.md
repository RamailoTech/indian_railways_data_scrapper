# Railway Data

This Python project is designed to scrape and process railway data from specific websites related to Indian Railways. 
The goal is to extract relevant information such as train number, station names, and other relevent information into a excel file.

### About

This project scrapes and processes railway data from Indian Railways websites using Selenium, and parses PDFs via Azure services. 
The extracted data is then cleaned and preprocessed to feed a language model (LLM) for identifying relevant information such as train numbers, station names, and stoppages.


### Key Features

- Web Scraping: Utilize selenium to extract structured data from Indian Railways websites.

* Data extraction: Download and extract data by parsing pdfs using azure service.

* Data Preprocessing: Clean and preprocess the parsed data to feed the LLM.

* Extract Information: Provide LLM the preprocessed text to extract relevant information like train numbers, names, stations, stoppages.

### Usage

1. Clone the repository:

`https://github.com/RamailoTech/Railway-Data.git`

2. Navigate to the project directory:

`cd Railway-Data`

3. Create a virtual environment:

`python3 -m venv venv`

4. Activate the virtual environment:

`source venv/bin/activate`

5. Install dependencies:

`pip install -r requirements.txt`

6. Create .env file and add openai key and azure credentials.

7. Run the bash script:

`./run_scripts.sh year`

    Note: Replace year with the specific year you want to work for. (Eg: 2023)

8. Generate combined data after generating data for all year.

   `python3 scripts/concat_excels.py`
