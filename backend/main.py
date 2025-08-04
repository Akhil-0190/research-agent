from fastapi import FastAPI, Query
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware
from agent_controller import ResearchAgent

app = FastAPI(title="Research Agent - Cluster 1")

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

# Allow frontend requests (adjust if deployed separately)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/agent")
def run_research_agent(q: str = Query(..., description="Your research question")):
    agent = ResearchAgent(query=q)
    output = agent.run()

    return {
        "original_query": q,
        "plan": agent.plan,
        "thought_log": agent.thought_log,
        "results": {
            "papers": output.get("papers", []),
            "summaries": output.get("summaries", []),
            "citations": output.get("citations", []),
            "hypothesis": output.get("hypothesis", ""),
            "report": output.get("report", {})
        }
    }
