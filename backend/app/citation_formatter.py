def to_apa(paper):
    authors = ", ".join(paper['authors'])
    year = paper['published'][:4]
    title = paper['title']
    link = paper['link']
    return f"{authors} ({year}). {title}. Retrieved from {link}"

def to_ieee(paper, index):
    authors = ", ".join(paper['authors'])
    title = paper['title']
    link = paper['link']
    year = paper['published'][:4]
    return f"[{index}] {authors}, \"{title},\" {year}. [Online]. Available: {link}"

def to_bibtex(paper, index):
    first_author_lastname = paper['authors'][0].split()[-1].lower()
    year = paper['published'][:4]
    key = f"{first_author_lastname}{year}"
    title = paper['title']
    authors = " and ".join(paper['authors'])
    link = paper['link']
    
    return f"""@article{{{key},
  title={{ {title} }},
  author={{ {authors} }},
  year={{ {year} }},
  url={{ {link} }}
}}"""
