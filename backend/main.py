from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File, Form
from pdf_reader import extract_text_from_pdf

from summarizer import generate_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str
    length: str= "medium"

@app.post("/summarize")
def summarize(data: TextRequest):

    summary = generate_summary(
        data.text,
        data.length
        )

    return {
        "summary": summary
    }
@app.post("/summarize-pdf")
async def summarize_pdf(
    file: UploadFile = File(...),
    length: str=Form("medium")
):

    text = extract_text_from_pdf(file.file)

    summary = generate_summary(
        text,
        length
    )

    return {
        "summary": summary
    }