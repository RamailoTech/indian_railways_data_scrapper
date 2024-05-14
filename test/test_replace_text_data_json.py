import json
import os

def update_json_with_text_files(json_file_path, text_files_dir, output_json_path):
    # Load the original JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Iterate over each test case in the JSON data
    for test_case in data['test_cases']:
        test_id = test_case['test_id']
        text_file_path = os.path.join(text_files_dir, f"{test_id}.json_output.txt")
        
        # Check if the corresponding text file exists
        if os.path.exists(text_file_path):
            # Read the text file
            with open(text_file_path, 'r') as text_file:
                new_text = text_file.read()
            
            # Replace the 'text' field with the content of the text file
            test_case['text'] = new_text
    
    # Save the modified JSON data into a new file
    with open(output_json_path, 'w') as output_file:
        json.dump(data, output_file, indent=4)


# Specify the paths
json_file_path = 'data/tests/test_cases_using_layoutmodel.json'
text_files_dir = 'data/tests/output_text'
output_json_path = 'data/tests/test_cases_layoutmodel.json'

# Call the function to update the JSON file
update_json_with_text_files(json_file_path, text_files_dir, output_json_path)
