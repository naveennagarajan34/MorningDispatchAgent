import feedparser


def get_top_news(limit=5):
    """
    Fetches top news headlines from The Hindu Tamil Nadu regional feed.
    """
    feed_url = "https://www.thehindu.com/news/national/tamil-nadu/feeder/default.rss"

    try:
        feed = feedparser.parse(feed_url)
        articles = []

        for entry in feed.entries[:limit]:
            # Clean summary text in case HTML tags are attached
            raw_summary = getattr(entry, "summary", "")
            clean_summary = raw_summary.split("<")[0].strip()

            articles.append({"title": entry.title, "summary": clean_summary})

        return articles
    except Exception as e:
        return [{"error": f"Failed to fetch news: {str(e)}"}]


if __name__ == "__main__":
    news = get_top_news(5)
    print("\n--- Tamil Nadu News (The Hindu) ---")
    for idx, item in enumerate(news, start=1):
        print(f"\n{idx}. {item.get('title')}")
        if item.get("summary"):
            print(f"   Summary: {item.get('summary')}")
