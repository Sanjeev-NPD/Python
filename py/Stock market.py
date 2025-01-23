import requests
from bs4 import BeautifulSoup

def scrape_funding_news():
    url = "https://news.google.com/rss/search?q=funding+india"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        for item in items:
            title = item.title.text.strip()
            print(f"Title: {title}")
            print("----")
            print(item)
            print("----")
            print("")

if __name__ == "__main__":
    scrape_funding_news()
