from deep_translator import GoogleTranslator

text = input("Enter English text: ")

translated_text = GoogleTranslator(
    source="en",
    target="ta"
).translate(text)

print("Original text:")
print(text)

print("Translated text:")
print(translated_text)