# spiritus-ai · Sophia
# Entry point for the FastAPI application.
# This file wires together the app, routes, and startup events.

from fastapi import FastAPI

app = FastAPI(
    title="spiritus-ai",
    description="Sophia — a RAG-powered oracle built from a living knowledge vault.",
    version="0.1.0",
)


@app.get("/api/health")
def health_check():
    return {"status": "alive", "message": "Sophia is here."}
