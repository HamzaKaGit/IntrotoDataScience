import camelot as cm
ls
#input_pdf = cm.read_pdf("https://www.undp.org/content/dam/india/docs/india_factsheet_economic_n_hdi.pdf",flavor='stream')
#"stream", "lattice"
input_pdf = cm.read_pdf("india_factsheet_economic_n_hdi.pdf",flavor='lattice',pages='1,2')
input_pdf

for n in input_pdf:
    print(n)

input_pdf[2].df

df = input_pdf[2].df.loc[11:14,1:3]
df
df = df.reset_index(drop = True)
df

df.columns = ["KPI","2001","2011"]
df
df.loc[:,["2001","2011"]] = df.loc[:,["2001","2011"]].astype(float)
df
df.to_csv("packt_output.csv")
ls

df.to_excel("packt_output_excel.xlsx")
ls

import pandas as pd
df2 = pd.read_csv("packt_output.csv")
df2
import seaborn as sns
df_melted = df.melt('KPI', var_name='year', value_name='percentage')
df_melted
sns.barplot(x = "KPI", y = "percentage", hue = "year", data = df_melted);

 