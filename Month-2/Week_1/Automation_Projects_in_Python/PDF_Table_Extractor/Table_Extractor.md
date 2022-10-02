## Library for extracting tables from PDFs
````python
import camelot as cm
````
## Giving Url of PDF
````python
input_pdf = cm.read_pdf("https://www.undp.org/content/dam/india/docs/india_factsheet_economic_n_hdi.pdf",flavor='stream')
````
### Hard coded Link of Pdf
````python
input_pdf = cm.read_pdf("india_factsheet_economic_n_hdi.pdf",flavor='lattice',pages='1,2')
````
### Displaying Table Extracted Files
````python
for n in input_pdf:
    print(n)
````
### Selecting Desired Table
````python
input_pdf[2].df
df = input_pdf[2].df.loc[11:14,1:3]
df = df.reset_index(drop = True)
df.columns = ["KPI","2001","2011"]
df.loc[:,["2001","2011"]] = df.loc[:,["2001","2011"]].astype(float)
````
### Converting the Table to CSV(Tabular) Format
````pyhton
df.to_csv("packt_output.csv")
````

### Converting the Table to Excel Sheet Format
````python
df.to_excel("packt_output_excel.xlsx")
````
## Importing Library for Data Framing
````python
import pandas as pd
````
### Reading the Data in Tabular From
````python
df2 = pd.read_csv("packt_output.csv")
````
## Importing Library for Data Visualization
````python
import seaborn as sns
````
## Data Visualization
````python
df_melted = df.melt('KPI', var_name='year', value_name='percentage')
df_melted
sns.barplot(x = "KPI", y = "percentage", hue = "year", data = df_melted);
````
