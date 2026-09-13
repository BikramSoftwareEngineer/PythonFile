from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    # User-Agent header prevents standard web request blocks
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        # Fetch web page content
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines and links (using Hacker News structure)
        headlines = []
        for span in soup.find_all("span", class_="titleline"):
            anchor = span.find("a")
            if anchor:
                title = anchor.get_text(strip=True)
                # Convert relative links into absolute URLs
                link = urljoin(url, anchor["href"])
                headlines.append((title, link))

        return headlines

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []


if __name__ == "__main__":
    # Example Target Site
    target_url = "https://news.ycombinator.com/"
    results = scrape_news(target_url)

    # Print extracted headlines and links
    print(f"Found {len(results)} headlines:\n" + "=" * 60)
    for index, (title, link) in enumerate(results, start=1):
        print(f"{index}. Headline: {title}")
        print(f"   Link:     {link}\n")