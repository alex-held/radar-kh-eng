from translate import Translator

translator = Translator(to_lang="en",  from_lang="uk")

def translate(message: str) -> str:
    translated : str = translator.translate(message)
    translated = _handle_special_translations(translated)
    return translated

def _handle_special_translations(translated: str) -> str:
    translations = {
        "TREVOGA": "ALARM"
    }

    for old, new in translations.items():
        translated = translated.replace(old, new)   

    return translated