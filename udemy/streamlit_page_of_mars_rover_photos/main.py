import streamlit as st
import requests

api_key = "NdapsuZzEAW9w1UXcFI80tDg3QSmu8cHci9RXR6f"
#url=(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")

url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key={api_key}"

#https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
# Make request
response = requests.get(url)
data = response.json()

print(data["photos"][1]["img_src"])
image_url = data["photos"][1]["img_src"]
title = "curiosity.png"
# print(title)
#
response2 = requests.get(image_url)
#
with open(title, "wb") as file:
    file.write(response2.content)

st.title("Photo taken by " + title.split('.')[0])
st.image(title)