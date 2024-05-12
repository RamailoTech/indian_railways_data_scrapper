import json
import csv
import pandas as pd


# Parse the JSON data
file_path = 'test/predicted_test_layoutmodel_with_subject.json'
with open(file_path, 'r') as file:
    data = json.load(file)

output_path = 'results/subject_test_cases_layoutmodel.csv'
# Open a CSV file to write into
# Extracting the test cases
test_cases = data['test_cases']

# Preparing lists to hold each column's data
test_ids = []
types = []
texts = []
expected_outputs = []
predicted_outputs = []

# Looping through each test case to extract information
for case in test_cases:
    test_ids.append(case['test_id'])
    types.append(case['type'])
    texts.append(case['text'])
    expected_outputs.append(json.dumps(case['expected_output']))  # Converting list/dict to string
    predicted_outputs.append(json.dumps(case['predicted_output']))  # Converting list/dict to string

# Creating a DataFrame
df = pd.DataFrame({
    'test_id': test_ids,
    'type': types,
    'text': texts,
    'expected_output': expected_outputs,
    'predicted_output': predicted_outputs
})

# Saving to CSV
df.to_csv(output_path, index=False)

print("CSV file has been created successfully.")