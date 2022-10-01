# Importing Required Packages
### For sending HTTP requests
````python
from requests import get
````
### For pulling data out of HTML and XML files
````python
from bs4 import BeautifulSoup
````
### For Argument Parsing
````python
import sys
````

#### Exception Handling
````python
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the  URL")
 ````


#### Creating a Function to Extract only Text from `<p>` Tags
````python
def get_only_text(url):
 """ 
  return the title and the text of the article
  at the specified url
 """
 page = get(url)
 soup = BeautifulSoup(page.content, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 #text = soup.text
 title = ' '.join(soup.title.stripped_strings)
 return title , text   
 ````
### Calling the function with the desired News URL
````python
url = "https://en.wikinews.org/wiki/Global_markets_plunge"
text = get_only_text(url)
````
### Numver of Words - Original Text
````python
len(text[1])
text[1]
````
### Impoting Packages for Summarization

```` python
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
````

### Printing the Summarized Text by Word Count
````python
text[1]
print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), word_count=100))
print("\n\nLength of the summarized text: " + str(len(str.split((summarize(repr(text[1]), word_count=100))))))
````

### Number of Words - Summarized Text
````python
#print ("Title : " + text[0])
#print ("Summary : ")
#print (summarize(repr(text[1]), ratio=0.1))
summarized_text = summarize(repr(text[1]), ratio=0.1)
len(str.split(summarized_text))
````
### Printing Keywords
````python
print ('\nKeywords:')
print (keywords(text[1], ratio=0.1, lemmatize=True))
````

