import requests
from io import BytesIO
import feedparser
import csv
import os

def fetch_rss():
    feeds = [
        'http://feeds.bbci.co.uk/news/rss.xml',
        'https://rss.cbc.ca/lineup/topstories.xml'
    ]

    all_articles = []

    for url in feeds:
        print(f"🔍 Fetching from {url}")
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            feed = feedparser.parse(BytesIO(response.content))
            for entry in feed.entries:
                article = {
                    'Title': entry.title.strip(),
                    'Published': entry.published.strip(),
                    'Link': entry.link.strip(),
                    'Summary': entry.title.strip()[:150] + '...'  # simple summary from title
                }
                all_articles.append(article)
        except Exception as e:
            print(f"❌ Failed to fetch from {url}: {e}")

    print(f"✅ Fetched {len(all_articles)} articles total.")
    return all_articles

def remove_duplicates(new_articles, csv_file='rss_news.csv'):
    if not os.path.exists(csv_file):
        return new_articles  # Nothing to compare to

    existing_links = set()
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_links.add(row['Link'])

    unique_articles = [a for a in new_articles if a['Link'] not in existing_links]
    print(f"🧹 Removed {len(new_articles) - len(unique_articles)} duplicates.")
    return unique_articles

def save_to_csv(articles, filename='rss_news.csv'):
    if not articles:
        print("⚠️ No new articles to save.")
        return

    file_exists = os.path.isfile(filename)
    keys = ['Title', 'Published', 'Link', 'Summary']

    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        if not file_exists:
            writer.writeheader()
        writer.writerows(articles)

    print(f"💾 Appended {len(articles)} new articles to {filename}")

if __name__ == "__main__":
    articles = fetch_rss()
    unique_articles = remove_duplicates(articles)
    save_to_csv(unique_articles)
