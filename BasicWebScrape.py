import requests

#Scrape the page
RawScrape = requests.get("test").text

#Split by line
Data = RawScrape.splitlines()

for x in Data:
    if "String" in x:
        print("Do Something")
