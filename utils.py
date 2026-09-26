def clean_text(text):
    """Remove unnecessary whitespace from text."""
    if text is None:
        return ""

    return " ".join(str(text).split())

def to_lowercase(text):
return text.lower()

def to_uppercase(text):
return text.upper()

def validate_text_length(text, max_length=10000):
    """Validate that text does not exceed the configured maximum length."""
    if len(text) > max_length:
        raise ValueError(
            f"Text exceeds the maximum allowed length of {max_length} characters."
        )

    return True
