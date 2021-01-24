import requests

api_key = "21e1aaf8c250543ca9d50018215c00cca4f09"
# the URL you want to shorten
url = input("Enter your long URL: ")

api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

data = requests.get(api_url).json()["url"]

if data["status"] == 7:
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)
