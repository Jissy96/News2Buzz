import feedparser
import csv
import os

# Google News Top Headlines RSS Feed (all news)
rss_url = "https://news.google.com/news/rss?hl=en-US&gl=US&ceid=US:en"
feed = feedparser.parse(rss_url)

# Master CSV file
csv_file = "google_news_master.csv"

# Step 1: Load existing data (if file exists)
existing_titles = set()
if os.path.exists(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_titles.add(row["Title"])

# Step 2: Prepare new rows (skip duplicates)
new_articles = []
for entry in feed.entries:
    if entry.title not in existing_titles:
        new_articles.append([
            entry.title,
            entry.published,
            entry.link,
            entry.summary
        ])
        existing_titles.add(entry.title)

# Step 3: Write to file (append or create)
file_exists = os.path.exists(csv_file)
with open(csv_file, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Title", "Published", "Link", "Summary"])  # Header
    writer.writerows(new_articles)

print(f"✅ Added {len(new_articles)} new articles to {csv_file}")
