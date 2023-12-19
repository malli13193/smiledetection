#3.languagetrans
#pip install googletrans==3.1.0a0

from googletrans import Translator, LANGUAGES

text = input("Enter text: ")
print("Supported languages:", LANGUAGES)
lang_code = input("Enter language code: ")

translator = Translator()
translated_text = translator.translate(text, src='en', dest=lang_code)

print(f"Translate English to {LANGUAGES[lang_code]}: {translated_text.text}")
