import requests

api_key = "f97d3b9b281b40bfaaab42757a60cf3c"
url=("https://newsapi.org/v2/everything?q=tesla&from="
     "2025-02-23&sortBy=publishedAt&apiKey=f97d3b9b281b40bfaaab42757a60cf3c")

# Make request
request = requests.get(url)

# Get dictionary with data
content =request.json()
print(content['articles'])

i=0
# Access the article
for article in content["articles"]:
    print(article['title'])
