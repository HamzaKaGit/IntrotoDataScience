# Importing Required Packages
### For sending HTTP requests to Ted Talk
````python
from requests import get
````
### For pulling data out of HTML and XML files
````python
from bs4 import BeautifulSoup
````
### Regular Expression pattern matching
````python
import re
````
### For Argument Parsing
````python
import sys
````
## Exception Handling
````python
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")
  ````
  ## Desired URL's
````python
url = "https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection"

url = "https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity"
````
## Requesting for Download the Video
````python
r = requests.get(url)
print("Download about to start")
content = r.content
soup = BeautifulSoup(r.content, features="lxml")
for val in soup.findAll("script"):
    if(re.search("pageProps",str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]

print("Downloading video from ..... " + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ..... " + file_name)


r = requests.get(mp4_url)

with open(file_name,'wb') as f:
  f.write(r.content)
  ````

### Alternate method
````python
 urlretrieve(mp4_url,file_name)
````
### Downlading Completed
````
print("Download Process finished")
````
