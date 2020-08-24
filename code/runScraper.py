from datetime import date
import os  # helper functions like check file exists
import datetime  # automatic file name
from datetime import date
import requests  # the following imports are common web scraping bundle
import re
from collections import defaultdict
from urllib.request import urlopen  # standard python module
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError
import idxScraper,articleScraper,connectMongo
import time

## Reference
#https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

## Establish Base Path
today_url = idxScraper.getTodayURL()
today_dt_str = date.today().strftime("%Y-%m-%d")

## Retrieve article links and scraper
links = idxScraper.getArticlesLinks([today_url])
print("{} article links are retrieved for today")

## Setup Mongo Connection
conn = connectMongo.connect_mongo('leMonde','news_article')

for i,link in enumerate(links):
    if i < 18:
        print("scraping {}th article".format(i))
        article = articleScraper.scrape_article(link)

        if article:
            print("{}th article has {} paragraphs".format(i,article.num_paragraphs))
            if article.num_paragraphs>0:
                # Create nested article object
                article= {
                    'date':today_dt_str,
                    'title':article.title,
                    'num_paragraphs': article.num_paragraphs,
                    'paragraphs': article.paragraphs
                     }

                #Insert article object directly into MongoDB via isnert_one
                result=conn.insert_one(article)
                #Print to the console the ObjectID of the new document
                print('Exported {}th article as {}'.format(i,result.inserted_id))
        ## Rest for a second before scraping the next one 
        time.sleep(1.3)
