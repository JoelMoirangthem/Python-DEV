import pandas as pd                          # Importing the pandas library for data manipulation and analysis
from bs4 import BeautifulSoup                # Importing BeautifulSoup for parsing HTML content
import requests                              # Importing requests to send HTTP requests
import pandas                                # (Redundant) Importing pandas again (already imported as pd)

site = 'https://growthlist.co/india-startups/'  # URL of the website to scrape data from
data = requests.get(site)                      # Sending a GET request to the website and storing the response
soup = BeautifulSoup(data.text,'html')         # Parsing the HTML content of the page using BeautifulSoup

Table = soup.find_all('table')[0]              # Finding the first table on the webpage
Table_Head = Table.find_all('th')              # Extracting all table header (<th>) elements
Table_Heading = [heading.text.strip() for heading in Table_Head]  # Getting clean text from each header element

df = pd.DataFrame(columns=Table_Heading)       # Creating an empty DataFrame with the extracted table headers as columns

column_data = Table.find_all('tr')             # Extracting all table rows (<tr>) from the table
for data in column_data[1:]:                   # Iterating through all rows except the header row
    r_data = data.find_all('td')               # Extracting all data cells (<td>) from the row
    ind_data = [s.text.strip() for s in r_data]  # Getting clean text from each data cell
    df.loc[len(df)] = ind_data                 # Adding the row data to the DataFrame

df.to_csv('INDIA_STARUPS FUNDING',index=False) # Saving the DataFrame as a CSV file without the index column
