import requests

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-01-08&sortBy=publishedAt&" \
      "apiKey=2fefe58e0cd543048668e2b02cf9889e"
api_key = "2fefe58e0cd543048668e2b02cf9889e"

# make request
request = requests.get(url)

# get dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article['title'])
    print(article['description'])
