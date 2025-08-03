from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Research Agent - Cluster 1")

app.include_router(router)
