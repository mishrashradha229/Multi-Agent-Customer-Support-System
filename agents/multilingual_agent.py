from deep_translator import GoogleTranslator


def translate_text(text, target_language="English"):

    if not text:
        return ""

    try:

        translated = GoogleTranslator(
            source="auto",
            target=target_language.lower()
        ).translate(text)

        return translated

    except Exception:

        return text