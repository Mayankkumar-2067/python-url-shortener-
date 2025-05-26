import requests

def shorten_url(long_url):
    # API endpoint where the request is sent
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"

    # Sending an HTTP GET request
    response = requests.get(api_url)

    # If the response is successful
    if response.status_code == 200:
        return response.text  # this will be the short URL
    else:
        return "Error: Unable to shorten the URL."

# --- Code for user input ---
if __name__ == "__main__":
    print("== Python URL Shortener ==")
    user_url = input("Enter the long URL: ")
    short_url = shorten_url(user_url)
    print("Shortened URL:", short_url)
