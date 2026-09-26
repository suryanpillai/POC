from utils import (
    clean_text,
    to_uppercase,
    to_lowercase,
    validate_text_length,
    count_punctuation,
    estimate_reading_time,
    get_word_frequency,
    count_sentences,
    count_paragraphs,
)

from config import APP_NAME, APP_VERSION, SEPARATOR


def show_banner():
    print(SEPARATOR)
    print(f"       {APP_NAME.upper()}")
    print(f"Version: {APP_VERSION}")
    print("Analyze your text with simple automation")
    print(SEPARATOR)


def analyze_text(text):
    digit_count = sum(char.isdigit() for char in text)
    words = text.split()
    uppercase_count = sum(char.isupper() for char in text)
    lowercase_count = sum(char.islower() for char in text)
    text_length = len(text)
    is_empty = not bool(text.strip())

    vowel_count = sum(
        char.lower() in "aeiou"
        for char in text
    )

    consonant_count = sum(
        char.isalpha() and char.lower() not in "aeiou"
        for char in text
    )

    space_count = text.count(" ")
    line_count = len(text.splitlines())

    longest_word = max(words, key=len) if words else ""
    shortest_word = min(words, key=len) if words else ""

    average_word_length = (
        sum(len(word) for word in words) / len(words)
        if words else 0
    )

    unique_word_count = len(
        set(word.lower() for word in words)
    )

    contains_question = "?" in text
    contains_exclamation = "!" in text

    punctuation_count = count_punctuation(text)
    reading_time = estimate_reading_time(text)
    word_frequency = get_word_frequency(text)
    sentence_count = count_sentences(text)
    paragraph_count = count_paragraphs(text)

    return {
        "word_count": len(words),
        "character_count": text_length,
        "uppercase_text": to_uppercase(text),
        "lowercase_text": to_lowercase(text),
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "reversed_text": text[::-1],
        "title_case_text": text.title(),
        "digit_count": digit_count,
        "uppercase_count": uppercase_count,
        "lowercase_count": lowercase_count,
        "is_empty": is_empty,
        "vowel_count": vowel_count,
        "consonant_count": consonant_count,
        "space_count": space_count,
        "line_count": line_count,
        "punctuation_count": punctuation_count,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "average_word_length": round(average_word_length, 2),
        "unique_word_count": unique_word_count,
        "word_frequency": word_frequency,
        "estimated_reading_time_minutes": reading_time,
        "contains_question": contains_question,
        "contains_exclamation": contains_exclamation,
    }


def get_text_input():
    text = input("\nEnter some text: ")
    validate_text_length(text)
    return clean_text(text)


def display_results(result):
    """Display analysis results in a readable format."""
    print("\nAI Automation Result")
    print(SEPARATOR)

    for key, value in result.items():
        display_key = key.replace("_", " ").title()
        print(f"{display_key}: {value}")


def main():
    show_banner()

    print("Welcome! Enter text to begin analysis.")

    text = get_text_input()

    if not text.strip():
        print("Please enter some valid text.")
        return

    result = analyze_text(text)
    display_results(result)

    print("\nThank you for using AI Text Automation Tool!")


if __name__ == "__main__":
    main()
