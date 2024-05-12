import os 
import openai
import json 
from encoding_scripts import get_policy_encoding_stoppage_results,get_policy_encoding_introduced_results,get_policy_encoding_extension_results
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
    file_path = 'test/test_cases_layoutmodel.json'
    output_file_path = 'test/predicted_test_layoutmodel_with_subject.json'
    
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
            # output = "None"
        # test_case['predicted_output'] = output
        
    # Write the modified data to a new file
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Updated JSON data with predicted outputs written to {output_file_path}.")






# text = """THE GENERAL MANAGER (OPTG) COPY TO: CPTM NWR/JAIPUR NWR/JAIPUR 09605 AJMER- JAIPUR DEMU 09605 AJMER - JAIPUR DEMU 1 STATIONS 1 09606 JAIPUR- AJMER DEMU 09606 JAIPUR- AJMER DEMU EXISTING TIMINGS APPROVED TIMINGS    EXISTING TIMINGS APPROVED TIMINGS 07:15 07:00 D AJMER A 23:15 23:15 10:15 09:45 09:50 A D JAIPUR D A 19:05 19:05 19:00 -- 11:05 11:15 A D DAUSA D A  17:35 17:25 -- 14:00 A GANGAPUR CITY D -- 15:00 DAYS OF OPERATION : EX- AJMER- MON, TUES, WED THUS, FRI & SAT EX- GANGAPUR- MON, TUES, WED THUS, FRI & SAT COMMERCIAL STOPPAGE ON THE EXTENDED PORTION : GANDHI NAGAR, GETOR JAGATPURA, KHATIPURA, BASSI, DAUSA, BANIYANA, NAGAL-RAJAWATAN, SALEMPUR ARNIYA KHURD, DEEDWANA, LALSOT, BINDORI, MANDAWARI, PIPLAI, BAMANWAS, KHUNTLA, UDAIKALAN PRIMARY MAINTENANCE : MADAR/ AJMER WITH RBPC"""
# type = "extension"
# output = get_results(text,type)
# print(output)