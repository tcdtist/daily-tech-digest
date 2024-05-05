import requests

def fetch_technology_news():
    api_key = '339588ce5b5587f98db0c6cf22c9038a'
    q = "developer"
    url = f"https://gnews.io/api/v4/search?q={q}&token={api_key}&lang=en&max=10&sortby=publishedAt"
    response = requests.get(url)
    articles = response.json()['articles']
    return articles

def update_readme(articles):
    with open('README.md', 'w') as f:
        f.write("# Technology News\n\n")
        for article in articles:
            f.write(f"## {article['title']}\n")
            f.write(f"{article['description']}\n")
            f.write(f"[Read more]({article['url']})\n\n")

def main():
    articles = fetch_technology_news()
    update_readme(articles)

if __name__ == "__main__":
    main()
