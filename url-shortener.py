import requests
import urllib.parse
from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def shorten_url(long_url):
    if not is_valid_url(long_url):
        return "Error: Invalid URL"

    encoded_url = urllib.parse.quote(long_url, safe='')
    api_url = f"https://tinyurl.com/api-create.php?url={encoded_url}"

    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: HTTP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("== Python URL Shortener ==")
    user_url = input("Enter the long URL: ").strip()
    short_url = shorten_url(user_url)
    print("Shortened URL:", short_url)