import os
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


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def serve_vue():
    index_path = os.path.join("static", "index.html")
    return FileResponse(index_path)


@app.post("/api/encode")
def encode_text(message: TextMessage):
    return {"result": encode(message.text)}


@app.post("/api/decode")
def decode_text(message: TextMessage):
    return {"result": decode(message.text)}
