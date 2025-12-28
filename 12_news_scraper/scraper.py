import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# Target URL
URL = "https://thehackernews.com/"

def fetch_news():
    print(f"[*] Fetching news from {URL}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = []
        
        # The Hacker News structure typically uses 'story-link' class or similar for container
        # We will look for <h2> class="home-title" which contains the title
        
        articles = soup.find_all('h2', class_='home-title')
        
        if not articles:
            print("[-] No articles found. The site structure might have changed.")
            return []

        for article in articles:
            title = article.get_text(strip=True)
            # Try to get link if possible (parent <a> tag usually)
            link = ""
            parent = article.find_parent('a')
            if parent and 'href' in parent.attrs:
                link = parent['href']
                
            news_items.append({
                "title": title,
                "link": link,
                "timestamp": datetime.now().isoformat()
            })
            
        return news_items

    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

def display_news(news):
    print("\n--- Latest Security News ---")
    for idx, item in enumerate(news, 1):
        print(f"{idx}. {item['title']}")
        print(f"   Link: {item['link']}")
        print("")

def save_news(news):
    filename = "news.json"
    try:
        with open(filename, "w") as f:
            json.dump(news, f, indent=4)
        print(f"[+] News saved to {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    news = fetch_news()
    if news:
        display_news(news)
        save_news(news)
    else:
        print("[-] No news retrieved.")

if __name__ == "__main__":
    main()
