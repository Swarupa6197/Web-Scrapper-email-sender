import requests
import re

def scrape_website(url, keyword=None):
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        content = response.text
    except Exception as e:
        return [f"Error fetching site: {e}"]

    # Try extracting headlines and paragraphs
    headlines = re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>", content, re.IGNORECASE)
    paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", content, re.IGNORECASE)

    results = headlines + paragraphs

    # Remove HTML tags
    results = [re.sub(r"<.*?>", "", text).strip() for text in results if text.strip()]

    # Filter by keyword
    if keyword:
        results = [r for r in results if keyword.lower() in r.lower()]

    return results[:30]  # top 30 results
