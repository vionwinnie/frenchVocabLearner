from datetime import date
import os  # helper functions like check file exists
import datetime  # automatic file name
from datetime import date
import requests  # the following imports are common web scraping bundle
import re,random,string
from collections import defaultdict
from urllib.request import urlopen  # standard python module
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError
import idxScraper,articleScraper,connectMongo_temp,connectFirestore
import time

## Reference
#https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

## Establish Base Path
today_url = idxScraper.getTodayURL()
today_dt_str = date.today().strftime("%Y-%m-%d")

## Retrieve article links and scraper
links,titles = idxScraper.getArticlesLinks([today_url])
print("{} article links are retrieved for today".format(len(links)))

## Set up database connection (MongoDb/Firestore)
sinkType = "firestore"
N=25
if sinkType == "firestore":
    conn = connectFirestore.connect('leMonde') 
elif sinkType== "mongoDb":
    conn = connectMongo_temp.connect_mongo('leMonde','news_article')
else:
    raise IndexError("Sink Type Not Specified")


for i,link in enumerate(links):
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
            if sinkType == "mongoDb":
                result=conn.insert_one(article)
            elif sinkType == "firestore":
                doc_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
                result = conn.document(doc_id).set(article)
                #Print to the console the ObjectID of the new document
                #print('Exported {}th article as {}'.format(i,result.inserted_id))
    ## Rest for a second before scraping the next one 
    time.sleep(1.3)
