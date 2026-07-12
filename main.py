from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File
from PyPDF2 import PdfReader
from utils import split_text_into_chunks

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import ollama
from translator import translate_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SentenceTransformer('all-MiniLM-L6-v2')

stored_chunks = []

index = None


class QuestionRequest(BaseModel):
    question: str
    language: str


@app.get("/")
def home():
    return {"message": "Python backend is working!"}


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    pdf = PdfReader(file.file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    chunks = split_text_into_chunks(text)

    global stored_chunks, index

    stored_chunks = chunks

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return {
        "message": "PDF processed, chunked, and embedded successfully!",
        "text": text[:1000],
        "total_chunks": len(chunks),
        "embedding_shape": str(embeddings.shape)
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    global stored_chunks, index

    if index is None:
        return {"answer": "Please upload a PDF first."}

    question_embedding = model.encode([request.question])

    distances, results = index.search(
        np.array(question_embedding),
        k=3
    )

    matched_chunks = []

    for i in results[0]:
        matched_chunks.append(stored_chunks[i])

    context = "\n\n".join(matched_chunks)

    response = ollama.chat(
        model='tinyllama',
        messages=[
            {
                'role': 'user',
                'content': f"""
Use this PDF context to answer the question.

Context:
{context}

Question:
{request.question}
"""
            }
        ]
    )

    ai_answer = response['message']['content']
    
    if request.language == "English":
        return {
            "answer": ai_answer
     }

    translated_answer = translate_text(ai_answer, request.language)

    return {
        "answer": translated_answer
    }