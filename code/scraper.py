from datetime import date
import os  # helper functions like check file exists
import datetime  # automatic file name
import requests  # the following imports are common web scraping bundle
import re
from collections import defaultdict
from urllib.request import urlopen  # standard python module
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

base_path="https://www.lemonde.fr/archives-du-monde"
today_date_str = date.today().strftime("%d-%m-%Y")
today_url = "{}/{}/".format(base_path,today_date_str)

def getArchiveLinks(daystart, dayend, monthstart, monthend):
    dates = [str(i).zfill(2)+"-"+str(j).zfill(2) +
             "-2019" for i in range(daystart, dayend) for j in range(monthstart, monthend)]
    archive_links = [
        "https://www.lemonde.fr/archives-du-monde/" + date + "/" for date in dates]
    return archive_links
archive_links = getArchiveLinks(1,29,1,9)
print(archive_links[:5])

def getArticlesLinks(archive_links):
    links_non_abonne = []
    for link in archive_links:
        html = None
        try:
            html = urlopen(link)
        except HTTPError as e:
            print("text url not valid", link)
        
        links_non_abonne = []

        if html:
            soup = BeautifulSoup(html, "html.parser")
            temp = soup.find_all(class_="teaser")
            for item in temp:
                # condition here : if no span sr-only (abonnes)
                if not item.find('span', {'class': 'sr-only'}):
                    links_non_abonne.append(item.find('a')['href'])
    return links_non_abonne

links = getArticlesLinks([today_url])
print(len(links))

def scrape_article(article_link):
    html = urlopen(article_link)
    if html:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("h1", {"class": "article__title"})
        if title:
            print(title.text)

        ## TODO: look for main text

    else:
        print("article not available")

import time

for i,link in enumerate(links):
    print("scraping {}th article".format(i))
    scrape_article(link)
    time.sleep(1.3)

