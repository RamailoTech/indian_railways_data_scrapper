# Check if the year argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <year>"
    exit 1
fi

# Set the year from the command line argument
year="$1"

# Define paths to your Python scripts
download_pdfs="scripts/download_pdfs.py"
scrape_table_data="scripts/scrape_railway_data.py"
filter_pdfs="scripts/filter_pdfs.py"
parse_json_script="scripts/get_json_to_text.py"
json_to_text="scripts/get_json_to_text.py"
llm_script="scripts/read_parsed_files_extract_data.py"
date_mapping="scripts/date_mapping.py"

# Run each Python script with the specified year as an argument
echo "Running scripts for year $year..."
echo "Executing $download_pdfs..."
python3 "$download_pdfs" "$year"
echo "Executing $scrape_table_data..."
python3 "$scrape_table_data" "$year"
echo "Executing $filter_pdfs..."
python3 "$filter_pdfs" "$year"
echo "Executing $parse_json_script..."
python3 "$parse_json_script" "$year"
echo "Executing $json_to_text..."
python3 "$json_to_text" "$year"
echo "Executing $llm_script..."
python3 "$llm_script" "$year"
echo "Executing $date_mapping..."
python3 "$date_mapping" "$year"

echo "All scripts for year $year have been executed."
