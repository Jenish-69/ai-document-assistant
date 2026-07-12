import streamlit as st
import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import ollama
import pyttsx3
import whisper
import sounddevice as sd
from scipy.io.wavfile import write

from utils import split_text_into_chunks
from translator import translate_text


st.title("AI Document Assistant")

st.write("Upload a PDF, type or speak a question, and get an AI answer.")


uploaded_file = st.file_uploader("Upload your PDF", type="pdf")


def record_audio(filename="audio/question.wav", duration=5, sample_rate=44100):

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

    write(filename, sample_rate, audio)


def transcribe_audio(filename="audio/question.wav"):

    model = whisper.load_model("base")

    result = model.transcribe(filename)

    return result["text"]


if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    chunks = split_text_into_chunks(text)
    st.subheader("Extracted Text")

    st.write(text[:2000])

    st.write("Total Chunks:", len(chunks))

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = embedding_model.encode(chunks)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    st.subheader("Ask Questions About the PDF")

    typed_question = st.text_input("Type your question")

    voice_question = ""

    if st.button("Record Voice Question"):

        st.info("Recording for 5 seconds...")

        record_audio()

        st.success("Recording complete!")

        voice_question = transcribe_audio()

        st.write("Voice Question:", voice_question)

    user_question = typed_question or voice_question

    if user_question:

        question_embedding = embedding_model.encode([user_question])

        question_embedding = np.array(question_embedding).astype("float32")

        k = 3

        distances, indices = index.search(question_embedding, k)

        retrieved_chunk = chunks[indices[0][0]]

        prompt = f"""
        Answer the question using only the context below.

        Context:
        {retrieved_chunk}

        Question:
        {user_question}
        """

        response = ollama.chat(
            model="tinyllama",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response["message"]["content"]

        st.subheader("AI Answer")

        st.write(answer)
        st.subheader("Translate Answer")

        language = st.selectbox(
            "Choose translation language",
            ["Tamil", "Hindi", "French", "Spanish"]
        )

        language_codes = {
            "Tamil": "ta",
            "Hindi": "hi",
            "French": "fr",
            "Spanish": "es"
        }

        if st.button("Translate Answer"):
            translated_answer = translate_text(answer, language_codes[language])
            st.write(translated_answer)

        st.subheader("Retrieved Chunk")

        st.write(retrieved_chunk)

        audio_path = "audio/answer.mp3"

        engine = pyttsx3.init()
        engine.save_to_file(answer, audio_path)
        engine.runAndWait()

        st.audio(audio_path)