#!/usr/bin/env python3 
'''This Python script, named **Emoji Decoder**, is designed to decode emojis from the text entered by a user. It leverages the capabilities of the emoji module and the Emoji API to interpret emojis and fetch additional related information. The script uses environment variables for API key management to enhance security.'''

import os
import requests
import emoji

def get_emoji_info(emoji_char):
    api_key = os.getenv('EMOJI_API_KEY')
    api_endpoint = f"https://emoji-api.com/emojis?access_key={api_key}&search={emoji_char}"
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            data = response.json()
            return data[0] if data else {"error": "No data found"}
        else:
            return {"error": f"API request failed with status code {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to reach Emoji API: {e}"}

def decode_emoji(user_text):
    decoded_info = []
    for char in user_text:
        if char in emoji.EMOJI_DATA['en']:
            emoji_info = get_emoji_info(char)
            decoded_info.append((char, emoji.demojize(char), emoji_info))
    return decoded_info

def main(user_text):
    return decode_emoji(user_text)

#TASKS, things to include (stretch goals):
    # tkinter:
    # flask:
    # dictionaries / lists / .get()
    # try / excerpt
    # pytest (homer(), test_homer(), asser homer())
    # checkout other PyPi packages - see what works with my current script
    # db sqlite3
    # bash scripting, loops, conditionals