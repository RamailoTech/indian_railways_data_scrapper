import os 
import openai
import json 
from scripts.encoding_scripts import get_policy_encoding_stoppage_results,get_policy_encoding_introduced_results,get_policy_encoding_extension_results
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")
openai.api_type = os.getenv("API_TYPE")



def process_text(input_text):
    # Replace newline characters '\n' with a space
    processed_text = input_text.replace('\n', ' ')
    return processed_text


def get_results(extracted_text,type):
    if type == "stoppage":
        encoded_data = get_policy_encoding_stoppage_results(extracted_text)
    elif type == "introduction":
        encoded_data = get_policy_encoding_introduced_results(extracted_text)
    elif type == "extension":
        encoded_data = get_policy_encoding_extension_results(extracted_text)
    return encoded_data


if __name__ == '__main__':
    file_path = 'data/tests/test_cases_layoutmodel.json'
    output_file_path = 'data/tests/predicted_test_layoutmodel_with_subject.json'
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    for test_case in data['test_cases']:
        type = test_case['type']
        extracted_text = test_case['text']
        extracted_text = process_text(extracted_text)
        try:
            output = get_results(extracted_text,type)
            test_case['predicted_output'] = output
        except Exception as e:
            print(extracted_text)
            print("Error during get_results:", e)
            output = "None"
            test_case['predicted_output'] = output

        
    # Write the modified data to a new file
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Updated JSON data with predicted outputs written to {output_file_path}.")




