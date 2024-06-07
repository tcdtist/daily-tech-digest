import requests
import os
from datetime import datetime

def fetch_technology_news():
    api_key = os.getenv('GNEWS_API_KEY')
    q = "developer"
    url = f"https://gnews.io/api/v4/search?q={q}&token={api_key}&lang=en&max=1&sortby=publishedAt"
    response = requests.get(url)
    articles = response.json()['articles']
    return articles

def update_readme(articles):
    with open('README.md', 'w') as f:
        f.write("# Technology News\n\n")
        f.write("[![Update README with Latest Tech News](https://github.com/tcdtist/daily-tech-digest/actions/workflows/main.yml/badge.svg)](https://github.com/tcdtist/daily-tech-digest/actions/workflows/main.yml)\n\n")
        for article in articles:
            f.write(f"## {article['title']}\n")
            f.write(f"{article['description']}\n")
            f.write(f"[Read more]({article['url']})\n\n")
        f.write(f"\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    articles = fetch_technology_news()
    update_readme(articles)

if __name__ == "__main__":
    main()
