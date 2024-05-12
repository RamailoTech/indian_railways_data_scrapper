#will have multiple lists with json
#concat the data
#create a single json
#extarct data and dump into excel
#also data type column

import json

# Sample data containing multiple lists of JSON objects
data = """
[
    [
        {
            "Train number": "None",
            "Train name": "20841 BHUBANESWAR-VISAKHAPATNAM VANDEBHARAT EXPRESS",
            "Start Station name": "BHUBANESWAR",
            "End Station name": "VISAKHAPATNAM",
            "Composition": {"VANDEBHARAT COACHES": 8},
            "Date of Issue": "11.03.2024"
        },
        {
            "Train number": "None",
            "Train name": "20842 VISAKHAPATNAM-BHUBANESWAR VANDEBHARAT EXPRESS",
            "Start Station name": "VISAKHAPATNAM",
            "End Station name": "BHUBANESWAR",
            "Composition": {"VANDEBHARAT COACHES": 8},
            "Date of Issue": "11.03.2024"
        }
    ],
    [
        {
            "Train number": "11239",
            "Train name": "MGR Chennai-Gaya Express",
            "Stoppage Station name": "Chanda Fort",
            "Date of Issue": "11.03.2024"
        },
        {
            "Train number": "18573/18574",
            "Train name": "Visakhapatnam-Bhagat Ki Kothi Express",
            "Stoppage Station name": "Ashoknagar",
            "Date of Issue": "11.03.2024"
        },
        {
            "Train number": "20482",
            "Train name": "Tiruchirappalli-Bhagat Ki Kothi Humsafar Express",
            "Stoppage Station name": "Mungaoli",
            "Date of Issue": "11.03.2024"
        },
        {
            "Train number": "19053/19054",
            "Train name": "Surat-Muzaffarpur Express",
            "Stoppage Station name": "Mungaoli",
            "Date of Issue": "11.03.2024"
        },
        {
            "Train number": "20971/20972",
            "Train name": "Udaipur-Shalimar Express",
            "Stoppage Station name": "None",
            "Date of Issue": "11.03.2024"
        },
        {
            "Train number": "18207/18208",
            "Train name": "Durg-Ajmer Express",
            "Stoppage Station name": "Mungaoli",
            "Date of Issue": "11.03.2024"
        },
        {
            "Train number": "20961/20962",
            "Train name": "Udhna-Banaras Express",
            "Stoppage Station name": "None",
            "Date of Issue": "11.03.2024"
        },
        {
            "Train number": "22193/22194",
            "Train name": "Daund-Gwalior Express",
            "Stoppage Station name": "Badarwas",
            "Date of Issue": "11.03.2024"
        }
    ]
]
"""

# Load JSON data
json_data = json.loads(data)

# Function to concatenate lists of JSON objects
def concatenate_lists(list_of_lists):
    combined_list = []
    for sublist in list_of_lists:
        combined_list.extend(sublist)
    return combined_list

# Combine the lists
combined_list = concatenate_lists(json_data)

# Optionally, convert the combined list back to JSON for storage or further processing
combined_json = json.dumps(combined_list, indent=4)

# Printing the combined JSON for demonstration
print(combined_json)



