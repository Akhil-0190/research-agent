from fastapi import APIRouter, Query
from app.granite_refiner import refine_query
from app.arxiv_search import search_arxiv
from app.citation_formatter import to_apa, to_ieee, to_bibtex
from app.summarizer import summarize_abstract, generate_hypothesis
from app.report_generator import generate_report

router = APIRouter()

@router.get("/search")
def search_papers(q: str = Query(..., description="Your research question")):
    refined = refine_query(q)
    papers = search_arxiv(refined)

    summaries = []
    for idx, paper in enumerate(papers, start=1):
        summary = summarize_abstract(paper["summary"])
        paper["summary_granite"] = summary
        summaries.append(summary)

        paper["citations"] = {
            "APA": to_apa(paper),
            "IEEE": to_ieee(paper, idx),
            "BibTeX": to_bibtex(paper, idx)
        }
    hypothesis = generate_hypothesis(summaries, refined)
    report = generate_report(refined, summaries, hypothesis)

    return {
        "original_query": q,
        "refined_query": refined,
        "results": papers,
        "paper_summaries": summaries,
        "generated_hypothesis": hypothesis,
        "auto_generated_report": report
    }