import requests

# Replace 'BOT_TOKEN' with your actual bot token
bot_token = 'BOT_TOKEN'

# URL for getting bot information via the Telegram Bot API
api_url = f"https://api.telegram.org/bot{bot_token}/getMe"

# Send the API request to get bot information
response = requests.get(api_url)

# Check the response status
if response.status_code == 200:
    data = response.json()
    bot_id = data['result']['id']
    print(f"Bot ID: {bot_id}")
else:
    print(f"Failed to get bot information. Response code: {response.status_code}")
