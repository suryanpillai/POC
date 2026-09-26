import string


def count_punctuation(text):
    """Count punctuation characters in text."""
    return sum(char in string.punctuation for char in text)

"punctuation_count": count_punctuation(text),

from collections import Counter


def get_word_frequency(text):
    """Return word frequency information for the supplied text."""
    words = text.lower().split()
    return dict(Counter(words))

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
