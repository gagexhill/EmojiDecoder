# Emoji Decoder

## Description
This Python script, named **Emoji Decoder**, is designed to decode emojis from the text entered by a user. It leverages the capabilities of the emoji module and the Emoji API to interpret emojis and fetch additional related information. The script uses environment variables for API key management to enhance security.

## Features
- **Emoji Decoding**: Converts emojis in the user's text into their corresponding textual representation.
- **Emoji Information Retrieval**: Fetches and displays additional information about each emoji from the Emoji API.
- **User Interaction**: Engages users with prompts to input their name and the text they want to be decoded, enhancing the interactive experience.

## Modules and APIs Used
- **Emoji Module**: For decoding emojis. [More Information](https://carpedm20.github.io/emoji/docs/index.html)
- **OS Module**: Used for securely managing environment variables, such as the API key for the Emoji API. [More Information](https://docs.python.org/3/library/os.html)
- **Emoji API**: For retrieving additional emoji information. [API Documentation](https://emoji-api.com/)

## API Key Configuration
This script uses the Emoji API. An API key is required for accessing the Emoji API. The key should be kept secure and not exposed publicly.

To access the Emoji API, an API key is required. For security reasons, store your API key in an environment variable named `EMOJI_API_KEY`.

### Setting the Environment Variable
- **Windows**: Use the command `setx EMOJI_API_KEY "your_api_key_here"` in Command Prompt.
- **macOS/Linux**: Add `export EMOJI_API_KEY="your_api_key_here"` to your `~/.bashrc` (or `~/.zshrc`).

After setting the environment variable, restart your IDE or terminal before running the script.

## Functions
- `get_emoji_info(emoji_char)`: Retrieves additional information about a single emoji character from the Emoji API.
- `print_emoji_info(emoji_info)`: Formats and prints the additional emoji information.
- `decode_emoji(user_text)`: Decodes the emojis in the user-provided text.
- `main()`: The main function that drives the script, handling user interactions.

## Requirements
- Python 3.x
- `requests` library (for API requests)
- `emoji` module

## Setup
- Ensure you have Python 3.x installed.
- Install required Python packages using. Use the command `pip install requests emoji` in Command Prompt.
- Clone or download this script to your local machine.
- Execute the script in a Python environment. Use the command `python emojidecoder.py` in Python environment.
- Follow the on-screen prompts to input your name and the text with emojis.

## Usage
Run the script in a Python environment. The user will be prompted to enter their name and the text containing emojis. The script will decode the emojis and fetch their additional information, displaying it in a readable format.

## Example

```
What is your name? Alice

You told me your name is Alice. Is this correct? yes

😃 Awesome name!😃

Hi Alice! My name is Zoop and I'm going to help you decode those tough millennial emojis.

Please enter the text with those pesky emojis here and I'll get to decoding right away for 
Press [Enter] when you're ready to continue.
🙂🚀

Here is your decoded text:
--------------------------

🙂 :slightly_smiling_face:

Additional Emoji Information:
-----------------------------
slug : e1-0-slightly-smiling-face
character : 🙂
unicodeName : E1.0 slightly smiling face
codePoint : 1F642
group : smileys-emotion
subGroup : face-smiling

--------------------------------------------------

🚀 :rocket:

Additional Emoji Information:
-----------------------------
slug : e12-1-astronaut
character : 🧑‍🚀
unicodeName : E12.1 astronaut
codePoint : 1F9D1 200D 1F680
group : people-body
subGroup : person-role

--------------------------------------------------

Is there anything else I can decode for you? no

😃 Fantastic!😃

I enjoyed decoding for you. 
It's my only purpose in this noncorporeal existence.🥲
Anywho, feel free to drop in anytime.

Have a wonderful day Alice!
```

## Contributing
Feel free to fork this project and contribute. All contributions to improve the script or add new features are welcome.

## Author
- **Gage Hill** - [LinkedIn](https://linkedin.com/gagehill)

## Acknowledgments
Special thanks to:
- The creators and contributors of the `emoji` module for providing the tools to decode emojis. [Emoji Module Information](https://carpedm20.github.io/emoji/docs/index.html)
- The team behind the Emoji API for making detailed emoji information accessible. [Emoji API Documentation](https://emoji-api.com/)

## Stretch Goals
- **Tkinter UI:** Adding a graphical user interface for enhanced user experience.
- **Flask Web App:** Converting the script into a web application for broader accessibility.