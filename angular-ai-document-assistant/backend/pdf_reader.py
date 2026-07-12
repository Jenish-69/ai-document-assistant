from pypdf import PdfReader
import pyttsx3

pdf_path = input("Enter your PDF file path: ")

reader = PdfReader(pdf_path)

all_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        all_text += text + "\n"

print("PDF text extracted successfully!")
print("Speaking PDF content...")

engine = pyttsx3.init()
engine.say(all_text)
engine.runAndWait()