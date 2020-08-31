## Idea: An Integrated Portal that I can store and learn French word systematically

## Functionality:
- (Optional): Scrape French article from LeMonde
- Display Text and Highlight words
- Look up words from Dictionary
- Review Vocabulary
- [Chatbot] Question and Answer based on Article?
- (Optional): Knowledge Graph between all articles

## Links:
- Scraping LeMonde:
   - https://medium.com/@xiaoouwang/scrape-lemonde-articles-for-testing-nlp-libraries-1-3b9fce1cd38f
	
## Technical Aspect
- Webscraper 
- Look Up words from French dictionary using Naive Implementation
- Store dictionary using Hashmap method?

## Roadmap
- Build webscraper backend using BeautifulSoup / Requests
- Implement Hashmap / Hash table 
- Talk to Hayk about Chatbot functionality

## Front end:
- Design Landing Page
	- Display available links on the day
- Design Reading Page
	- Highlight functions, pop up box for annotations
	- Blank for summarization
- Design Review Page
	- Display by Article
	- Display by Part of Speech

## Create Local Testing Environment
- `conda create -n frenchVocab python=3.7 pip`
- `conda activate frenchVocab`
- `pip install -r requirements.txt`

## how to test the model using the interactive shell
- `python manage.py shell`
- `from learner.models import Lemonde`
- `articles = Lemonde.collection.fetch()`
- `for article in articles:
        print(article.title)   `

