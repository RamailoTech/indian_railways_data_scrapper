import pandas as pd
import json

# Load the CSV file
df = pd.read_csv('results/subject_test_cases_layoutmodel.csv')

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
df.to_csv('results/subject_cases_evaluation_layoutmodel.csv', index=False)




# import pandas as pd
# import json

# #1 if true, 0 if false

# # Load the CSV file
# df = pd.read_csv('results/test_cases_layoutmodel.csv')

# # Function to compare lengths
# def compare_lengths(expected, predicted):
#     try:
#         expected_json = json.loads(expected)
#         predicted_json = json.loads(predicted)
#         return 1 if len(expected_json) == len(predicted_json) else 0
#     except json.JSONDecodeError:
#         return 0  

# df['length_match'] = df.apply(lambda row: compare_lengths(row['expected_output'], row['predicted_output']), axis=1)


# def compare_json_fields(exp_output, pred_output, field): 
#     try:
#         expected = json.loads(exp_output)
#         predicted = json.loads(pred_output)
        
#         # Check if expected and predicted are unexpectedly still strings (double-encoded JSON)
#         if isinstance(expected, str):
#             expected = json.loads(expected)
#         if isinstance(predicted, str):
#             predicted = json.loads(predicted)

#         # Ensure that both are lists of dictionaries
#         expected = [item if isinstance(item, dict) else {} for item in expected]
#         predicted = [item if isinstance(item, dict) else {} for item in predicted]

#         all_matches = True
#         one_match = False

#         # Collect fields present in any dictionary
#         exp_fields = {key for item in expected if isinstance(item, dict) for key in item.keys()}
#         pred_fields = {key for item in predicted if isinstance(item, dict) for key in item.keys()}

#         # If field not present in both expected and predicted, return None
#         if field not in exp_fields and field not in pred_fields:
#             return None, None

#         for exp_item in expected:
#             exp_field = exp_item.get(field)
#             match_found = False
#             for pred_item in predicted:
#                 pred_field = pred_item.get(field)
#                 # Perform case-insensitive comparison
#                 if exp_field.strip().lower() == pred_field.strip().lower():
#                     match_found = True
#                     one_match = True
#                     break
#             if not match_found:
#                 all_matches = False

#         return int(all_matches), int(one_match)
#     except json.JSONDecodeError:
#         return None, None


# # Sample DataFrame application logic
# fields = ["Train number", "Train name", "Start Station name", "End Station name", "Stoppage Station name", "Date of Issue"]
# prefixes = ["all_", "one_"]
# suffixes = ["_matches"]

# for field in fields:
#     df[[f"{prefixes[0]}{field.lower().replace(' ', '_')}{suffixes[0]}",
#         f"{prefixes[1]}{field.lower().replace(' ', '_')}{suffixes[0]}"]] = df.apply(
#         lambda x: compare_json_fields(x["expected_output"], x["predicted_output"], field), axis=1, result_type='expand').astype(pd.Int32Dtype())

# # To save the updated dataframe to a CSV
# df.to_csv('results/test_cases_evaluation_layoutmodel.csv', index=False)




