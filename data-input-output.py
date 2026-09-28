import pandas as pd


# CSV
#----------------------------------------------




df = pd.read_csv("example.csv")
# print(df)

df.to_csv("My_output",index=False)

# print(pd.read_csv("My_output"))






# EXCEL
#----------------------------------------------



df = pd.read_excel("Excel_Sample.xlsx", sheet_name="Sheet1")
# print(df)

df.to_excel("Excel_output.xlsx", sheet_name="Sheet1")




# HTML
#----------------------------------------------


# data = pd.read_html("https://www.fdic.gov/bank/individual/failed/banklist.html")
# print(type(data))


# print(data)




# SQL
#----------------------------------------------

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table', engine)
sqldf = pd.read_sql('my_table', con=engine)
# print(sqldf)






















