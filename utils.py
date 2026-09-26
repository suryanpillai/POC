def clean_text(text):
    """Remove unnecessary whitespace from text."""
    if text is None:
        return ""

    return " ".join(str(text).split())

def to_lowercase(text):
return text.lower()

def to_uppercase(text):
return text.upper()
