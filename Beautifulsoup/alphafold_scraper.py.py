import requests
from bs4 import BeautifulSoup
import time

def fetch_articles(query, start):
    url = f"https://scholar.google.com/scholar?start={start}&q={query}&hl=en&as_sdt=0,5"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.text

def parse_articles(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("div", class_="gs_ri")
    results = []

    for article in articles:
        title = article.find("h3", class_="gs_rt").find("a").text
        author_info = article.find("div", class_="gs_a").text
        snippet = article.find("div", class_="gs_rs").text

        results.append({
            "title": title,
            "author_info": author_info,
            "snippet": snippet
        })

    return results

def main():
    query = "alphafold+Canada"
    num_pages = 5
    all_results = []

    for i in range(num_pages):
        start = i * 10
        print(f"Fetching page {i+1}...")
        html = fetch_articles(query, start)
        results = parse_articles(html)
        all_results.extend(results)
        time.sleep(2)

    print(f"Found {len(all_results)} articles:")
    for result in all_results:
        print(f"Title: {result['title']}\nAuthor Info: {result['author_info']}\nSnippet: {result['snippet']}\n")

if __name__ == "__main__":
    main()
