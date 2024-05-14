import openai
import json
from utils import *


def get_policy_encoding_stoppage_results(extracted_text,model_name = 'gpt-3.5-turbo',  prompt = get_system_prompt_encoding_stoppage(), guidelines = get_encoding_guidelines()):
    '''
        model_name: str
            The name of the model
        text: str
            The text of the Railway data

        system_prompt: The prompt to be passed to the model
    '''
    user_input = f"""
    Railway data: ```{extracted_text}```
    {guidelines}
    """
    response = openai.chat.completions.create(
            model = model_name,
            messages=[
                {"role": "system","content": prompt},
                {
                    "role": "user",
                    "content": user_input,
                }
            ],temperature=0,max_tokens=4095)
    
    response_content = response.choices[0].message.content
    start_index = response_content.find("[")
    end_index = response_content.rfind("]")
    response_content = response_content[start_index : end_index + 1]
    response_content_json = json.loads(response_content)
    return response_content_json


def get_policy_encoding_introduced_results(extracted_text,model_name = 'gpt-3.5-turbo',  prompt = get_system_prompt_encoding_introduced(), guidelines = get_encoding_guidelines()):
    '''
        model_name: str
            The name of the model
        text: str
            The text of the Railway data

        system_prompt The prompt to be passed to the model
    '''
    user_input = f"""
    Railway data: ```{extracted_text}```
    {guidelines}
    """
    response = openai.chat.completions.create(
            model = model_name,
            messages=[
                {"role": "system","content": prompt},
                {
                    "role": "user",
                    "content": user_input,
                }
            ],temperature=0,max_tokens=4095) 
    
    response_content = response.choices[0].message.content
    start_index = response_content.find("[")
    end_index = response_content.rfind("]")
    response_content = response_content[start_index : end_index + 1]
    response_content_json = json.loads(response_content)
    return response_content_json


def get_policy_encoding_extension_results(extracted_text,model_name = 'gpt-3.5-turbo',  prompt = get_system_prompt_encoding_extension(), guidelines = get_encoding_guidelines()):
    '''
        model_name: str
            The name of the model
        text: str
            The text of the Railway data

        system_prompt The prompt to be passed to the model
    '''
    user_input = f"""
    Railway data: ```{extracted_text}```
    {guidelines}
    """
    response = openai.chat.completions.create(
            model = model_name,
            messages=[
                {"role": "system","content": prompt},
                {
                    "role": "user",
                    "content": user_input,
                }
            ],temperature=0,max_tokens=4095)
    
    response_content = response.choices[0].message.content
    start_index = response_content.find("[")
    end_index = response_content.rfind("]")
    response_content = response_content[start_index : end_index + 1]
    response_content_json = json.loads(response_content)
    return response_content_json
