import requests

url = input()
website = requests.get(url)
text = website.text
with open("index.html", "w") as f:
    f.write(text)