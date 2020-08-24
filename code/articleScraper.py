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


class Article:

    def __init__(self):
        self.paragraphs = None
        self.title = None
        self.num_paragraphs = 0

def scrape_article(article_link=None,local_file_path=None):
    
    html = None

    if article_link:
        html = urlopen(article_link)
        if html:
            soup = BeautifulSoup(html, "html.parser")

        else:
            print("article not available")


    if local_file_path:
        f = open(local_file_path, encoding="utf8")
        soup = BeautifulSoup(f,features="html.parser")
        f.close()

    if soup:
        this_article = Article()
        
        ## Extract Title
        title = soup.find("h1", {"class": "article__title"})
        if title:
            this_article.title=title.text
        
        ## Extract Main Paragraphs
        #article_text = soup.find("article",{"class":"article__content old__article-content-single"})

        all_paragraph = soup.findAll("p",{"class":"article__paragraph"})
        if len(all_paragraph)>0:
            this_article.num_paragraphs= len(all_paragraph)
            paragraph_text = []
            for paragraph in all_paragraph:
                paragraph_text.append(paragraph.text)

            this_article.paragraphs = paragraph_text
        
        return this_article
    else:
        return None

if __name__ == "__main__":
    data_folder= "/home/winnie/petProjects/frenchVocabLearner/frenchVocabLearner/raw_data"
    data_file_name = "sample_text.html"

    data_file_path = data_folder + "/" + data_file_name
    scrape_article(local_file_path=data_file_path)


