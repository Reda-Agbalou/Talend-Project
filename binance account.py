# Binance API endpoints
import requests
import time
import hashlib
import hmac
import json

# Replace these with your actual Binance API key and secret
api_key = 'vyxuEXlHAHPxT4AnEjIXk1CRzjLjTmJ66B8HNxZJrrBkTTdwWkbOJBxJ5cqF9xS5'
api_secret = 'ZTFBP0U0siSoY9X7J9t3niMtugB2TXpYJR2m0u3BMex5lpRZIWbHmOnRMbl5UI8T'
base_url = 'https://api.binance.com/api/v3'
endpoint = '/account'

# Create the API request headers
headers = {
    'X-MBX-APIKEY': api_key
}
def get_binance_account_info():
    try:
        # Add timestamp to the request
        timestamp = int(time.time() * 1000)  # Convert to milliseconds
        params = {'timestamp': timestamp}

        # Create a signature for the request
        query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
        signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
        params['signature'] = signature

        # Make a GET request to Binance API
        response = requests.get(base_url + endpoint, headers=headers, params=params)
        response.raise_for_status()  # Check for errors

        # Parse the response
        account_info = response.json()

        # Save the data to a JSON file
        with open('c:\\Users\\RPC\\Desktop\\bi\\data\\binance_account_info.json', 'w') as file:
            json.dump(account_info, file, indent=2)

        print("Binance Account Info saved to binance_account_info.json")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing Binance API: {e}")
if __name__ == "__main__":
    get_binance_account_info()