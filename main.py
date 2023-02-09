import requests
import os
from send_email import send_email

api_key = os.getenv("NEWSAPIKEY")
topic = "steam deck"

url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2023-01-08&sortBy=publishedAt&" \
      f"apiKey={api_key}&language=en"

# make request
request = requests.get(url)

# get dictionary with data
content = request.json()

# Access the article titles and descriptions
msg = "Subject: News App \n"
for article in content["articles"][:20]:
    if article['title'] is not None:
        msg += article['title'] + "\n"
        msg += article['description'] + "\n"
        msg += article['url'] + "\n" + "\n"


send_email(msg)



