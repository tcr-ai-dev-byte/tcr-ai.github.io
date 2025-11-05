# main.py
# Minimal-Backend für TCR.AI mit FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# ---- App-Grundgerüst
app = FastAPI(title="TCR.AI API", version="0.1.0")

# ---- CORS: erlaube Aufrufe von deiner GitHub-Pages-Domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tcr-ai-dev-byte.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Datenmodell für /generate
class Prompt(BaseModel):
    text: str

# ---- Healthcheck (zum schnellen Testen im Browser)
@app.get("/health")
def health():
    return {"ok": True}

# ---- Demo-Endpoint: später ersetzt du die Logik durch dein LLM
@app.post("/generate")
def generate(p: Prompt):
    reply = f"TCR.AI Demo antwortet auf: {p.text[:120]}"
    return {"response": reply}
