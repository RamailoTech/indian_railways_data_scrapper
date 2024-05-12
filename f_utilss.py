
def get_system_prompt_encoding_stoppage():
    system_prompt = """
    
    **Task Overview:**
    Encode the provided Railway text data containing Stoppage of train service information  into a JSON object adhering to the specified structure. Ensure you follow these detailed instructions:

    1. **Extract the information from the given text data.**
    The text data will contain the following information in subject, paragraphs or table format seperated by | operator:

    - Train number : This field typically refers to a unique identifier assigned to a specific train service. Eg: 20957/58. Note that the train number is greater than 4 digits.
    - Train name : This field indicates the name or title of the train service. It's usually descriptive and may include the origin-destination details. Eg: Indore-New Delhi Express, Valsad-Vadnagar Express. Also donot provide extra information in train name such as 'Howrah-Titlagarh Ispat Express (Tri-Weekly)'. Also ensure to provide full train name. 
    - Stoppage Station name : This field lists the name of a station where the train makes a scheduled stop. Eg: Delhi
    - Date of Issue : This field specifies the date when this railway information was issued or generated.Eg: 01.03.2024


    2.  **JSON Structure**:
    - The JSON object should have the following format:
    ```
        [
            {
                "Train number":Train number,
                "Train name":Train name,
                "Stoppage Station name":Stoppage Station name,
                "Date of Issue":Date of Issue
            }
        ]
    ```
    Note: If the input text specifies multiple train numbers or name, (e.g.,'"13413/14 and 13483/84"' or '01861/01862, 01863/01864, 01865/01866, 01867/01868')the system should generate separate JSON objects for each train number or name. Donot generate the output by separating with "and" or commas(,) in any json field. Ensure to provide every train details mentioned in table.

    ```
    [
        {
            "Train number":Train number,
            "Train name":Train name,
            "Stoppage Station name":Stoppage Station name,
            "Date of Issue":Date of Issue
        },
        {
            "Train number":Train number,
            "Train name":Train name,
            "Stoppage Station name":Stoppage Station name,
            "Date of Issue":Date of Issue
        }
    ]
    ```
    ### Railway Data example:

    **Example 1:**

    ```
    NO. 2024/CHG/22/10 (.) MINISTRY OF RAILWAYS DESIRES THAT EXPERIMENTAL STOPPAGE OF THE FOLLOWING TRAIN(s) SHOULD BE PROVIDED AT THE STATION(s) AND WITH EFFECT FROM THE DATE(s) INDICATED ALONGSIDE (.)

    A CLOSE WATCH SHOULD BE KEPT AT THE SALE OF TICKETS AT THE STATION(s) FOR REVIEW (.) GIVE WIDE PUBLICITY (.) ENSURE COMPLIANCE AND CONFIRM (.)

    Tabular data:

    Table 1:
    THE GENERAL MANAGERs (OPTG.)|COPY TO: CPTMs
    WR/ MUMBAI|WR/ MUMBAI
    WCR/JABALPUR|WCR/JABALPUR
    NCR/PRAYAGRAJ|NCR/PRAYAGRAJ
    NWR/JAIPUR|NWR/JAIPUR
    NR/NEW DELHI|NR/NEW DELHI

    Table 2:
    SL|TRAIN NO. AND NAME|STATION|W.E.F.
    1.|20957/58 INDORE-NEW DELHI EXPRESS|KHACHROD|EARLY CONVENIENT DATE
    2.|12925/26 MUMBAI CENTRAL- AMRITSAR PASCHIM EXPRESS|KHACHROD|EARLY CONVENIENT DATE
    3.|19711/12 JAIPUR-BHOPAL EXPRESS|TARANA ROAD|EARLY CONVENIENT DATE


    ```

    - **Output JSON:**
    [
        {
            "Train number":"20957/58",
            "Train name":"Indore-New Delhi Express",
            "Stoppage Station name":"Khachrod",
            "Date of Issue":"None"
        },
        {
            "Train number":"12925/26",
            "Train name":"Amritsar Paschim Express",
            "Stoppage Station name":"Khachrod",
            "Date of Issue":"None"
        },
        {
            "Train number":"19711/12",
            "Train name":"Jaipur-Bhopal Express",
            "Stoppage Station name":"Tarana Road",
            "Date of Issue":"None"
        }
    ]
    """
    return system_prompt


def get_system_prompt_encoding_introduced():
    system_prompt = """
    **Task Overview:**
    Encode the provided Railway text data containing Introduction of new train service information  into a JSON object adhering to the specified structure. Ensure you follow these detailed instructions:

    1. **Extract the information from the given text data.**
    The text data will contain the following information in subject, paragraphs or table format seperated by | operator:

    - Train number : This field typically refers to a unique identifier assigned to a specific train service. Eg: 20957/58. Note that the train number is greater than 4 digits.
    - Train name : This field indicates the name or title of the train service. It's usually descriptive and may include the origin-destination details. Eg: Indore-New Delhi Express. Also donot provide extra information in train name such as 'Howrah-Titlagarh Ispat Express (Tri-Weekly)'. Also ensure to provide full train name.
    - Start Station name : This field lists the name of a station from where the train service starts. Eg: Indore
    - End Station name : This field lists the name of a station from where the train service starts. Eg: Delhi
    - Composition : This field contain information about type of train's composition. Eg: coaches, 
    - Date of Issue : This field specifies the date when this railway information was issued or generated. Eg: 12.02.2024

    
    2.  **JSON Structure**:
    - The JSON object should have the following format:
    ```
        [
            {
                "Train number":Train number,
                "Train name":Train name,
                "Start Station name":Start Station name,
                "End Station name":End Station name,
                "Composition":{
                    "Type1": 2,
                    "Type2": 4
                },
                "Date of Issue":Date of Issue
            }
        ]

    ```
    
    Note: If the composition is not mentioned then add "None" in the JSON field. If the input text specifies multiple train numbers or name ,  (e.g.,  '"13413/14 and 13483/84"' or '01861/01862, 01863/01864, 01865/01866, 01867/01868')the system should generate separate JSON objects for each train number or name. Donot generate the output by separating with "and" or commas(,) in any json field. Also ensure to generate different json when the train number and train name is same but the station name is different.

    ```
    [
        {
            "Train number":Train number,
            "Train name":Train name,
            "Start Station name":Start Station name,
            "End Station name":End Station name,
            "Composition":{
                "Type1": 2,
                "Type2": 4
            },
            "Date of Issue":None
        },
        {
            "Train number":Train number,
            "Train name":Train name,
            "Start Station name":Start Station name,
            "End Station name":End Station name,
            "Composition":{
                "Type1": 2,
                "Type2": 4
            },
            "Date of Issue":None
        }
    ]
    ```

    ### Railway Data example:

    **Example 1:**

    ```
    NO. 2023/CHG/16/ECR/24(.) CONNECT ECR'S LETTER NO. ECR/OPT/TT/510/NEW TRAIN DATED 20.01.2024 REGARDING INTRODUCTION OF NEW TRAIN FROM RAXAUL TO JOGBANI VIA DARBHANGA, JHANJHARPUR AND SARAIGARH (.) MINISTRY OF RAILWAYS APPROVES INTRODUCTION OF NEW TRAIN BETWEEN RAXAUL AND JOGBANI AS UNDER :-

    THE ABOVE INTRODUCTION SHOULD BE GIVEN EFFECT FROM EARLY CONVENIENT DATE UNDER ADVICE TO THIS OFFICE (.) IF REQUIRED, THE TRAINS MAY BE PLANNED AS A SPECIAL SERVICE WHICH SHALL PICK UP ITS LINK SUBSEQUENTLY (.) GIVE WIDE PUBLICITY (.) ENSURE COMPLIANCE AND ACTION ACCORDINGLY (.) MATTER MOST URGENT (.)

    Tabular data:

    Table 1:
    THE GENERAL MANAGERs (OPTG)|COPY TO: CPTMs
    ECR/HAJIPUR|ECR/HAJIPUR
    NFR/GUWAHATI|NFR/GUWAHATI

    Table 2:
    RAXAUL-JOGBANI EXPRESS|1|STATION|1|JOGBANI-RAXAUL EXPRESS
    12.40|D|RAXAUL|A|11.15
    14.52/14.57|A/D|SITAMARHI|A/D|08.55/09.00
    16.35/17.05|A/D|DARBHANGA|A/D|06.30/07.00
    17.28/17.30|A/D|SAKRI|A/D|04.55/05.00
    18.00/18.02|A/D|JHANJHARPUR|A/D|04.00/04.05
    19.10/19.12|A/D|SARAIGARH|A/D|02.45/02.50
    19.50/20.20|A/D|LALITGRAM|A/D|01.25/01.55
    21.15/22.00|A/D|FORBESGANJ|A/D|00.10/00.50
    22.30|A|JOGBANI|D|23.45

    Table 3:
    PRIMARY MAINTENANCE|:|RAXAUL
    FREQUENCY|:|BI-WEEKLY EX. RAXAUL-MONDAY & THURSDAY EX. JOGBANI-MONDAY & THURSDAY
    COMMERCIAL STOPPAGE|:|GHORASAHAN,SITAMARHI, DARBHANGA, SAKRI, JHANJHARPUR, GHOGHARDIHA, NIRMALI, SARAIGARH, RAGHOPUR, LALITGRAM, NARPATGANJ, FORBESGANJ
    COMPOSITION||2 SLR, 4 GS, 5 GSCN, 1 ACCN=TOTAL 12 COACHES


    ```

    - **Output JSON:**

    [
        {
            "Train number":"None",
            "Train name":"RAXAUL-JOGBANI EXPRESS",
            "Start Station name":"RAXAUL",
            "End Station name":"JOGBANI",
            "Composition":{
                "SLR": "2",
                "GS": "4",
                "GSCN": "5",
                "ACCN": "1"
            },
            "Date of Issue":"None"
        },
        {
            "Train number":"None",
            "Train name":"JOGBANI-RAXAUL EXPRESS",
            "Start Station name":"JOGBANI",
            "End Station name":"RAXAUL",
            "Composition":{
                "SLR": "2",
                "GS": "4",
                "GSCN": "5",
                "ACCN": "1"
            },
            "Date of Issue":"None"
        }
    ]
    """
    return system_prompt



def get_system_prompt_encoding_extension():
    system_prompt="""
    **Task Overview:**
    Encode the provided Railway text data containing Extension of  train service information into a JSON object adhering to the specified structure. 

    Ensure you follow these detailed instructions:

    1. **Extract the information from the given text data.**
    The text data will contain the following information in subject, paragraphs or table format seperated by | operator:

    - Train number : This field typically refers to a unique identifier assigned to a specific train service. Eg: 20957/58. Note that the train number is greater than 4 digits.
    - Train name : This field indicates the name or title of the train service. It's usually descriptive and may include the origin-destination details. Eg: Indore-New Delhi Express. Also donot provide extra information in train name such as 'Howrah-Titlagarh Ispat Express (Tri-Weekly)' should be just 'Howrah-Titlagarh Ispat Express'. 
    - End Station name : This field lists the name of a station where the train service end or makes a scheduled stop. Eg: Delhi. Note that the end station can be different for different train names.
    - Date of Issue : This field specifies the date when this railway information was issued or generated.Eg: 01.03.2024


    2.  **JSON Structure**:
    - The JSON object should have the following format:
    ```
    [
        {
            "Train number":Train number,
            "Train name":Train name,
            "End Station name":End Station name,
            "Date of Issue":Date of Issue
        }
    ]
    ```

    Note: If the input text specifies multiple train numbers or name , (e.g., '"13413/14 and 13483/84"' or '01861/01862, 01863/01864, 01865/01866, 01867/01868')the system should generate separate JSON objects for each train number or name. Donot generate the output by separating with "and" or commas(,) in any json field. Also ensure to generate different json when the train number and train name is same but the station name is different.

    ```
    [
        {
            "Train number":Train number1,
            "Train name":Train name1,
            "End Station name":End Station name1,
            "Date of Issue":Date of Issue
        },
        {
            "Train number":Train number2,
            "Train name":Train name2,
            "End Station name":End Station name2,
            "Date of Issue":Date of Issue
        }
    ]
    ```

    ### Railway Data example:

    **Example 1:**

    ```
    (.) CONNECT CENTRAL RAILWAY'S LETTER NO. T.649.A/37/MR/XIII/D DATED 21.01.2024 REGARDING EXTENSION OF 11401/02 CHHATRAPATI SHIVAJI MAHARAJ (T)-ADILABAD NANDIGRAM EXPRESS UPTO BALHARSHAH (.) MINISTRY OF RAILWAYS APPROVES EXTENSION OF 11401/02 CHHATRAPATI SHIVAJI MAHARAJ (T)-ADILABAD NANDIGRAM EXPRESS UPTO BALHARSHAH TO THE FOLLOWING ABSTRACT TIMINGS (.)

    THE ABOVE EXTENSION MAY BE GIVEN EFFECT FROM AN EARLY CONVENIENT DATE UNDER ADVICE TO THIS OFFICE (.) ENSURE COMPLIANCE AND ACTION ACCORDINGLY (.) GIVE WIDE PUBLICITY (.) MATTER MOST URGENT (.)

    Tabular data:

    Table 1:
    THE GENERAL MANAGERs (OPTG.)|COPY TO: CPTMs
    CR/MUMBAI|CR/MUMBAI
    SCR/SECUNDERABAD|SCR/SECUNDERABAD

    Table 2:
    11401 CHHATRAPAT I SHIVAJI MAHARAJ (T)- ADILABAD NANDIGRAM EXPRESS|11401 CHHATRAPAT I SHIVAJI MAHARAJ (T)- BALHARSHAH NANDIGRAM EXPRESS|1|STATIONS|1|11402 BALHARSHAH CHHATRAPAT I SHIVAJI MAHARAJ (T) NANDIGRAM EXPRESS|11402 ADILABAD - CHHATRAPATI SHIVAJI MAHARAJ (T) NANDIGRAM EXPRESS
    EXISTING TIMINGS|APPROVED TIMINGS||||APPROVED TIMINGS|EXISTING TIMINGS
    16:35|16:35|D|CHHATRAPATI SHIVAJI MAHARAJ (T)|A|05:35|05:35
    09:30|09:25 09:30|A D|ADILABAD|D A|13:05 13:00|13:00
    |13:45|A|BALHARSHAH|D|08:30|

    Table 3:
    PRIMARY MAINTENANCE|..|BALHARSHAH WITH RBPC
    COMMERCIAL STOPPAGES ON THE EXTENDED PORTION|:|PIMPAL KHUTI, WANI, BHANDAK, CHANDRAPUR
    ```

    - **Output JSON:**
    [
        {
            "Train number": "11401",
            "Train name":"CHHATRAPAT I SHIVAJI MAHARAJ (T)- BALHARSHAH NANDIGRAM EXPRESS",
            "End Station name":"BALHARSHAH",
            "Date of Issue":"None"
        },
        {
            "Train number": "11402",
            "Train name":"CHHATRAPAT I SHIVAJI MAHARAJ (T)- ADILABAD NANDIGRAM EXPRESS",
            "End Station name":"BALHARSHAH",
            "Date of Issue":"None"
        }
    ]
    """
    return system_prompt

def get_encoding_guidelines():
    guideline = """
    Guidelines
    1. Ensure all parts of this structure are populated precisely from the provided text.
    2. Do not add any new. The information must be extracted from the provided data only.
    3. If the information is not provided in the given text then add "None" in the json field.
    4. Ensure that the provided output is STRICTLY in  JSON format and there are no missing information.
    5. STRICTLY ensure that there are no missing delimiter in the output JSON.
    6. Do not provide any Extra information such as code blocks (```) in the output.
    7. Ensure that the spellings are correct.
    8. Ensure to include accurately all the information provided in knowledge source.
    """
    return guideline


