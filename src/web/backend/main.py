from fastapi import FastAPI
from pydantic import BaseModel

from encoding.encoder import encode
from encoding.decoder import decode


class TextMessage(BaseModel):
    text: str


app = FastAPI()


@app.post("/encode")
def encode_text(message: TextMessage):
    return {"result": encode(message.text)}


@app.post("/decode")
def decode_text(message: TextMessage):
    return {"result": decode(message.text)}
