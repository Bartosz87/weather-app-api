import requests
from send_email import send_email
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)

api_key = "f97d3b9b281b40bfaaab42757a60cf3c"
url=(f"https://newsapi.org/v2/everything?q=tesla&from="
     f"{yesterday}&sortBy=publishedAt&apiKey=f97d3b9b281b40bfaaab42757a60cf3c")

# Make request
request = requests.get(url)

# Get dictionary with data
content =request.json()
# print(content)
# print(content.keys())
# print(content["articles"])

i=0
# Access the article
article_number = 1
body = ""
for article in content["articles"][0:30]:
    body = body +str(article_number) +") " + article['title'] +". Published at " + article['publishedAt'][0:-10] + "\n"
    article_number = article_number +1

message = '''\
Subject: Latest 30 articles overview
''' + "\n" + body

message = message.encode("utf-8")

send_email(message)
#print(message.decode("utf-8"))
