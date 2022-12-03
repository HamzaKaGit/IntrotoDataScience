
import Glassdoor_Scrapper as gs 
import pandas as pd 

path = "G:/ByteWise/Final_Project/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)