import pandas as pd
import json

# Load the CSV file
df = pd.read_csv('data/tests/subject_test_cases_layoutmodel.csv')

def all_fields_match(expected, predicted, field):
    try:
        expected_json = json.loads(expected)
        predicted_json = json.loads(predicted)

        # Ensure that both are lists of dictionaries
        expected = [item if isinstance(item, dict) else {} for item in expected_json]
        predicted = [item if isinstance(item, dict) else {} for item in predicted_json]

        # Collect the specific field values from both expected and predicted JSON
        expected_values = list([item.get(field, "").strip().lower() for item in expected])
        predicted_values = list([item.get(field, "").strip().lower() for item in predicted])

        # Check if all predicted values match the expected values
        return 1 if expected_values == predicted_values else 0
    except json.JSONDecodeError:
        return 0

# Applying the function for each required field and creating a new column for each
df['total_number_of_trains_predicted'] = df.apply(lambda x: all_fields_match(x['expected_output'], x['predicted_output'], 'Train number'), axis=1)
df['train_start_station_matched'] = df.apply(lambda x: all_fields_match(x['expected_output'], x['predicted_output'], 'Start Station name'), axis=1)
df['train_end_station_matched'] = df.apply(lambda x: all_fields_match(x['expected_output'], x['predicted_output'], 'End Station name'), axis=1)
df['train_stoppage_station_matched'] = df.apply(lambda x: all_fields_match(x['expected_output'], x['predicted_output'], 'Stoppage Station name'), axis=1)
df['date_of_issue_matched'] = df.apply(lambda x: all_fields_match(x['expected_output'], x['predicted_output'], 'Date of Issue'), axis=1)

# Save the updated dataframe to a CSV
df.to_csv('data/tests/subject_cases_evaluation_layoutmodel.csv', index=False)




