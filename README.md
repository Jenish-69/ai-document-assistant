# 🤖 AI Document Assistant

An intelligent AI-powered document assistant that enables users to upload PDF documents, ask natural language questions, translate responses into multiple languages, and interact using both speech and text.

Built with **FastAPI**, **Angular**, **FAISS**, **Sentence Transformers**, and **Ollama (TinyLlama)**, this project demonstrates the implementation of Retrieval-Augmented Generation (RAG), multilingual translation, speech recognition, and text-to-speech in a modern full-stack application.

---

## 📌 Features

- 📄 Upload PDF documents
- 🔍 Extract text from uploaded PDFs
- 🧠 AI-powered Question Answering using Retrieval-Augmented Generation (RAG)
- 🌍 Translate AI responses into multiple languages
  - English
  - Tamil
  - Hindi
  - Malayalam
- 🎤 Speech-to-Text (Voice Input)
- 🔊 Text-to-Speech (Voice Output)
- ⚡ FastAPI REST API backend
- 🎨 Angular frontend with an interactive user interface

---

# 🏗️ System Architecture

```
                PDF Upload
                     │
                     ▼
          Text Extraction (PyPDF)
                     │
                     ▼
      Sentence Transformer Embeddings
                     │
                     ▼
              FAISS Vector Store
                     │
                     ▼
            Retrieve Relevant Chunks
                     │
                     ▼
          Ollama (TinyLlama LLM)
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
    AI Generated Answer    Translation
          │
          ▼
     Text-to-Speech
          │
          ▼
      User Response
```

---

# 🛠️ Tech Stack

### Frontend

- Angular
- TypeScript
- HTML
- CSS

### Backend

- FastAPI
- Python
- Uvicorn

### AI & Machine Learning

- Ollama (TinyLlama)
- Sentence Transformers
- FAISS
- Retrieval-Augmented Generation (RAG)

### NLP

- Hugging Face Transformers
- Multilingual Translation Models

### Speech

- Speech-to-Text (STT)
- Text-to-Speech (TTS)

### PDF Processing

- PyPDF2

---

# 📂 Project Structure

```
ai-document-assistant/
│
├── angular-ai-document-assistant/
│   ├── frontend/
│   └── backend/
│
├── tests/
│
├── app.py
├── main.py
├── pdf_reader.py
├── translator.py
├── utils.py
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/Jenish-69/ai-document-assistant.git
```

```bash
cd ai-document-assistant
```

---

## 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate it

### Windows

```bash
myenv\Scripts\activate
```

### Linux / macOS

```bash
source myenv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Install Ollama and pull the TinyLlama model.

```bash
ollama pull tinyllama
```

Ensure the Ollama server is running.

---

## 5. Run the FastAPI backend

```bash
uvicorn main:app --reload
```

Backend will start at

```
http://127.0.0.1:8000
```

---

## 6. Run the Angular frontend

Navigate to the frontend folder.

```bash
cd angular-ai-document-assistant/frontend
```

Install packages.

```bash
npm install
```

Run Angular.

```bash
ng serve
```

Frontend will be available at

```
http://localhost:4200
```

---

# 📷 Screenshots

Add screenshots of:

- Home Page
- Upload PDF
- AI Question Answering
- Translation
- Speech-to-Text
- Text-to-Speech

---

# 🔄 Workflow

1. Upload a PDF document.
2. Extract document text.
3. Convert text into embeddings.
4. Store embeddings using FAISS.
5. Ask questions related to the document.
6. Retrieve relevant document chunks.
7. Generate contextual responses using TinyLlama.
8. Translate the response (optional).
9. Listen to the answer using Text-to-Speech.

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Retrieval-Augmented Generation (RAG)
- Large Language Model integration
- REST API development
- Angular frontend development
- FastAPI backend development
- Vector databases (FAISS)
- Sentence embeddings
- Speech processing
- PDF parsing
- Multilingual AI applications
- End-to-end AI application development

---

# 🚀 Future Improvements

- OCR support for scanned PDFs
- Multiple PDF support
- Chat history
- User authentication
- Cloud deployment
- More LLM support (Llama 3, Gemma, Mistral)
- Better multilingual support
- Document summarization
- Citation highlighting

---

# 👨‍💻 Author

**Jenish Jebaraj**

Computer Science Engineering Student

Passionate about Artificial Intelligence, Machine Learning, Full Stack Development, and Building Intelligent Applications.

GitHub:
https://github.com/Jenish-69

LinkedIn:
(Add your LinkedIn profile)

---

## ⭐ If you found this project interesting, consider giving it a star!
