import requests
import xml.etree.ElementTree as ET

def search_arxiv(query: str, max_results=5):
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results
    }

    response = requests.get(url, params=params)
    root = ET.fromstring(response.text)

    papers = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()
        summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip()
        authors = [author.find("{http://www.w3.org/2005/Atom}name").text.strip()
                   for author in entry.findall("{http://www.w3.org/2005/Atom}author")]
        published = entry.find("{http://www.w3.org/2005/Atom}published").text.strip()
        link = entry.find("{http://www.w3.org/2005/Atom}id").text.strip()

        paper = {
            "title": title,
            "summary": summary,
            "authors": authors,
            "published": published,
            "link": link
        }
        papers.append(paper)
    
    return papers
