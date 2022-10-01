# Importing Packages
## For http Requests
````python 
import requests
````
## For Web Scrapping
````python 
from bs4 import BeautifulSoup
````
## For Sending Mail
````python 
import smtplib
````
## For Mail Body
````python 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
````
## For System Date and Time Manipulation
````python 
import datetime
now = datetime.datetime.now()
````

# Email Content Placeholder
````python
content = ''
````


# Extracting Hacker News Stories
````python
def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>Hacker Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='More' else '')
        #print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
    return(cnt)
    
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content +=('<br><br>End of Message')
````
# lets send the Email
#### *make sure to update the Google Low App Access settings before
````python
print('Composing Email...')
````
### Your smtp server
````python
SERVER = 'smtp.gmail.com'
````
### Your port number
````python
PORT = 587
````
### Your FROM email id
````python
FROM =  'xyz@abc.com' 
````
## Your TO email ids  
#### can also be a list
````python
TO = 'abc@xyz.com' 
````
### Your email id's password
````python
PASS = '********' 
````
## Create a text/plain message
````python
msg = MIMEMultipart()
msg['Subject'] = 'Top News Stories [AI-Generated Mail by Hamza]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
    now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()

````



