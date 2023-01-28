import requests
import os
from bs4 import BeautifulSoup

name = "Boondock Saints" #define the name of the script you want to download
url = "https://imsdb.com/scripts/" + name + ".html"
folder = "scripts" #define the folder you want to save your scripts to

try:
    response = requests.get(url)
except requests.exceptions.RequestException as err:
    print ("Somethinf went wrong", err)
# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

elements = soup.find_all(class_="scrtext")
if not elements:
    raise Exception("No script by the following url not found")
else:
# Extract the text from the elements
    text = [element.get_text() for element in elements]

# Join the text into a single string
    text = "\n".join(text)

#create and save to folder
if not os.path.exists(folder):
    os.makedirs(folder)

file_path = os.path.join(folder, name)

with open(file_path, "w") as f:
    f.write(text)