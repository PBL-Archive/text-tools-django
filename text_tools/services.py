import re
import string
from string import punctuation

def remove_white_spaces(text):
    text = re.sub(r"[^\S\r\n]", " ", text, flags=re.DOTALL)
    return text

def remove_special_characters(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def remove_html_tags(text):
    text = re.sub(r"<[^>]*>", " ", text)
    return text

def remove_multiple_newlines(text):
    text = re.sub(r"(\n\s*)+\n", "\n", text)
    return text

def identify_emails(text):
    extracted_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    text = "\n".join(extracted_emails)
    return text

def identify_urls(text):
    extracted_urls = re.findall(r"(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])", text, re.IGNORECASE)
    text = "\n".join(extracted_urls)
    return text

def convert_to_camelcase(text):
    text = text.title()
    return text

def convert_to_pascalcase(text):
    text = ''.join(x for x in text.title() if not x.isspace())
    return text

def convert_to_snakecase(text):
    text = ''.join(['_'+c.lower() if c.isupper() else c for c in text]).lstrip('_')
    return text

def uppercase_full_text(text):
    text = text.upper()
    return text

def lowercase_full_text(text):
    text = text.lower()
    return text