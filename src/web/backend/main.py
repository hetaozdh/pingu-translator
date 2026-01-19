from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from encoding.encoder import encode
from encoding.decoder import decode
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Pingu Translator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextMessage(BaseModel):
    text: str


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR, html=True), name="static")


@app.get("/")
def serve_vue():
    index_path = STATIC_DIR / "index.html"
    return FileResponse(index_path)


@app.post("/api/encode")
def encode_text(message: TextMessage):
    return {"result": encode(message.text)}


@app.post("/api/decode")
def decode_text(message: TextMessage):
    return {"result": decode(message.text)}


@app.get("/{full_path:path}")
def spa_fallback(full_path: str):
    if full_path.startswith("api/"):
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="API endpoint not found")
    return FileResponse(STATIC_DIR / "index.html")
