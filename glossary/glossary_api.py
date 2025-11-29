from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
from typing import List, Optional

app = FastAPI()

# Load glossary data
with open("glossary.json", "r", encoding="utf-8") as f:
    glossary_data = json.load(f)

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.get("/api/terms")
def get_terms(query: Optional[str] = None):
    if query:
        query_lower = query.lower()
        filtered = [
            term for term in glossary_data
            if query_lower in term["term"].lower() or query_lower in term["definition"].lower()
        ]
        return filtered
    return glossary_data

@app.get("/api/terms/{term_id}")
def get_term(term_id: str):
    for term in glossary_data:
        if term["id"] == term_id:
            return term
    raise HTTPException(status_code=404, detail="Term not found")

@app.get("/api/graph")
def get_graph():
    nodes = []
    links = []
    
    for term in glossary_data:
        nodes.append({
            "id": term["id"],
            "label": term["term"]
        })
        
        for related in term.get("related_terms", []):
            links.append({
                "source": term["id"],
                "target": related,
                "type": "related"
            })
    
    return {
        "nodes": nodes,
        "links": links
    }

app.mount("/static", StaticFiles(directory="static"), name="static")



