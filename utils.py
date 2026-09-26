"""Utility functions for AI Text Automation."""

import string
from collections import Counter

from config import MAX_INPUT_LENGTH


def clean_text(text):
    """Remove unnecessary whitespace from text."""
    if text is None:
        return ""

    return " ".join(str(text).split())


def to_lowercase(text):
    """Convert text to lowercase."""
    return text.lower()


def to_uppercase(text):
    """Convert text to uppercase."""
    return text.upper()


def validate_text_length(text, max_length=MAX_INPUT_LENGTH):
    """Validate that text does not exceed the configured maximum length."""
    if len(text) > max_length:
        raise ValueError(
            f"Text exceeds the maximum allowed length of "
            f"{max_length} characters."
        )

    return True


def count_punctuation(text):
    """Count punctuation characters in text."""
    return sum(
        char in string.punctuation
        for char in text
    )


def estimate_reading_time(text, words_per_minute=200):
    """Estimate reading time in minutes."""
    if words_per_minute <= 0:
        raise ValueError(
            "Words per minute must be greater than zero."
        )

    words = len(text.split())

    if words == 0:
        return 0

    return round(
        words / words_per_minute,
        2
    )


def get_word_frequency(text):
    """Return word frequency information."""
    words = text.lower().split()
    return dict(Counter(words))


def count_sentences(text):
    """Count sentences using common sentence-ending punctuation."""
    normalized_text = (
        text.replace("!", ".")
        .replace("?", ".")
    )

    sentences = [
        sentence.strip()
        for sentence in normalized_text.split(".")
        if sentence.strip()
    ]

    return len(sentences)


def count_paragraphs(text):
    """Count non-empty paragraphs."""
    paragraphs = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]

    return len(paragraphs)
