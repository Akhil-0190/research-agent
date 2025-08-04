def format_citations(paper, idx):
    authors = ", ".join(paper["authors"])
    
    apa = f"{authors} ({paper['published'][:4]}). {paper['title']}."
    ieee = f"[{idx}] {authors}, \"{paper['title']}\", {paper['published']}."
    bibtex = (
        f"@article{{paper{idx},\n"
        f"  title={{ {paper['title']} }},\n"
        f"  author={{ {authors} }},\n"
        f"  year={{ {paper['published'][:4]} }},\n"
        f"  url={{ {paper['link']} }}\n"
        f"}}"
    )
    
    return {
        "APA": apa,
        "IEEE": ieee,
        "BibTeX": bibtex
    }
