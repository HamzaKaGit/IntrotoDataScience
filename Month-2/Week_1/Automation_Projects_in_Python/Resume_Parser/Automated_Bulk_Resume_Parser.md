## Importing Libraries
````python
#For Natural Language Processing
import spacy 
#For Converting Pdf
import pdfminer
#For Regular Expression
import re
#For File Manipulation
import os
#For Converting to Tabular Format
import pandas as pd
import pdf2txt
````
### Function to Convert PDF to Text
````python
def convert_pdf(f):

    output_filename = os.path.basename(os.path.splitext(f)[0]) + '.txt'
    #output_filepath = os.path.join('..', 'data', 'output', output_filename)
    output_filepath = os.path.join('Output/txt/', output_filename)
    #logging.info('Writing text from {} to {}'.format(f, output_filepath))
    pdf2txt.main(args=[f, '--outfile', output_filepath])
    print(output_filepath + " saved successfully!!!")
    return open(output_filepath).read()
````
### Loading the Language Model
````python
nlp = spacy.load("en_core_web_sm")
````
### Creating Output File Structure
````python
result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []}
names = []
phones = []
emails = []
skills = []
````
### Extracting Content From Resume
````python
def parse_content(text):
    skillset = re.compile('python|java|sql|hadoop|tableau')
    phone_num = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ is 'PERSON'][0]
    print(name)
    email = [word for word in doc if word.like_email == True][0]
    print(email)
    phone = str(re.findall(phone_num,text.lower()))
    skills_list = re.findall(skillset,text.lower())
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Extraction completed successfully!!!")
  ````
### Parsing Multiple Resumes
   ```` python
for file in os.listdir('Resumes/'):
    if file.endswith('.pdf'):
        print('Reading.....' + file)
        txt = convert_pdf(os.path.join('Resumes/',file))
        parse_content(txt)
  ````
### Putting Key Values in File Structure and then Displaying it
   ````python
 result_dict['name'] = names
result_dict['phone'] = phones
result_dict['email'] = emails
result_dict['skills'] = skills
print(result_dict)
````
### Displaying in Tabular Format

  ```python
result_df = pd.DataFrame(result_dict)
print(result_df)
````
### Converting in CSV file
````python
result_df.to_csv('Output/csv/parsed_resumes.csv')
````
