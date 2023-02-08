import requests
import os
from send_email import send_email

api_key = os.getenv("NEWSAPIKEY")
topic = "steam deck"

url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2023-01-08&sortBy=publishedAt&" \
      f"apiKey={api_key}"

# make request
request = requests.get(url)

# get dictionary with data
content = request.json()

# Access the article titles and descriptions
msg = ""
for article in content["articles"][:15]:
    if article['title'] is not None:
        msg += article['title'] + "\n"
        msg += article['description'] + "\n"
        msg += article['url'] + "\n" + "\n"


message = f"Subject: Email News App \n {msg}"
send_email(message)



