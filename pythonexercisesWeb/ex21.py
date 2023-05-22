#!usr/bin/python

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)


inpt= input("tell me what file name to save it to")

with open(inpt,"w") as file:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            file.write(story_heading.a.text.replace("\n", " ").strip())
        else:
            file.write(story_heading.contents[0].strip())



        