import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as file:
  csv_writer = writer(file)
  csv_writer.writerow(["Title", "Link", "Date"])

  for article in articles:
    anchor = article.find("a")

    title = anchor.get_text()
    date = article.find("time")["datetime"]
    url = anchor["href"]

    csv_writer.writerow([title, url, date])
