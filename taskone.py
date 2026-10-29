import requests
import csv
with open ('books.csv', 'w',newline="", encoding="utf-8-sig") as file:
     writer = csv.writer(file)
url = "https://openlibrary.org/search.json"

param = {
    'q' : 'python'
    ,
    'limit':50
}

response = requests.get(url,params=param)
data = response.json()

with open ('books.csv', 'w',newline="", encoding="utf-8-sig") as file:
     writer = csv.writer(file)
     writer.writerow(['book','First Published'])
     for i  in data['docs'] :
         year = (i.get('first_publish_year'))
         if year is  not None and  year > 2000 :
             title = (i.get('title'))
             writer.writerow([title,year])
            
          