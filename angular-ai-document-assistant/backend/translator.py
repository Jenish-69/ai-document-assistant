from deep_translator import GoogleTranslator

def translate_text(text, language):
    if language == "English":
        return text

    language_codes = {
        "Tamil": "ta",
        "Hindi": "hi",
        "Malayalam": "ml"
    }

    target_code = language_codes.get(language)

    if target_code is None:
        return text

    translated_text = GoogleTranslator(
        source="auto",
        target=target_code
    ).translate(text)

    return translated_text