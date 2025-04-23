import requests  # Import the requests module to make API calls

# Function to get the current price of a cryptocurrency
def coin_details(crypto):
    site = 'https://api.coingecko.com/api/v3/simple/price'  # API endpoint URL

    # Parameters to pass with the request (crypto ID and currency)
    details = {
        "ids": crypto,             # ID of the crypto (like 'bitcoin')
        'vs_currencies': 'inr'     # Currency to convert into (here, Indian Rupee)
    }
    
    # Try to fetch the price using the API
    try:
        # Make a GET request to the API with parameters
        response = requests.get(site, params=details, timeout=5)

        # Raise an error if the response is not successful (e.g., 404, 500)
        response.raise_for_status()

        # Parse the JSON response from the API
        data = response.json()

        # Extract the price in INR for the given crypto
        price = data[crypto]['inr']

        # Return the formatted result
        return f'Current price of {crypto} is Rs {price:.3f}'

    # Handle any request-related errors (like network or timeout)
    except requests.exceptions.RequestException as e:
        print(f'Error : Network or Http error : {e}')

# Ask user to input the name of a cryptocurrency
crypto = input("Enter the crypto name like bitcoin : ").strip().lower()

# Call the function and display the price
print(coin_details(crypto))
