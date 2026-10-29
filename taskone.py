
import requests
import csv

url = "https://openlibrary.org/search.json"

params = {
    "q": "python",
    "limit": 50,
}

response = requests.get(url, params=params)
data = response.json()

with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Book", "First Published"])

    for book in data["docs"]:
        year = book.get("first_publish_year")

        if year is not None and year > 2000:
            title = book.get("title", "Unknown")
            writer.writerow([title, year])
