import requests
import feedparser

def search_papers(query: str, max_results=3):
    base = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance"
    }
    response = requests.get(base, params=params)
    feed = feedparser.parse(response.text)
    papers = []
    for entry in feed.entries:
        papers.append({
            "title": entry.title,
            "summary": entry.summary,
            "authors": [author.name for author in entry.authors],
            "link": entry.link,
            "published": entry.published
        })
    return papers
