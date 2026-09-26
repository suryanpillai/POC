import csv
import json
import logging
import os
from datetime import datetime

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

from config import (
    APP_NAME,
    APP_VERSION,
    SEPARATOR,
    DEFAULT_ENCODING,
    DEFAULT_OUTPUT_FILE,
    DEFAULT_CSV_FILE,
    OUTPUT_DIRECTORY,
    HISTORY_FILE,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def show_banner():
    """Display the application banner."""
    print(SEPARATOR)
    print(f"       {APP_NAME.upper()}")
    print(f"Version: {APP_VERSION}")
    print("Analyze your text with simple automation")
    print(SEPARATOR)


def analyze_text(text):
    """Analyze the supplied text and return structured results."""
    digit_count = sum(
        char.isdigit()
        for char in text
    )

    digits_found = [
        char
        for char in text
        if char.isdigit()
    ]

    alphabetic_count = sum(
        char.isalpha()
        for char in text
    )

    words = text.split()

    uppercase_count = sum(
        char.isupper()
        for char in text
    )

    lowercase_count = sum(
        char.islower()
        for char in text
    )

    text_length = len(text)

    is_empty = not bool(
        text.strip()
    )

    vowel_count = sum(
        char.lower() in "aeiou"
        for char in text
    )

    consonant_count = sum(
        char.isalpha()
        and char.lower() not in "aeiou"
        for char in text
    )

    space_count = text.count(" ")

    line_count = len(
        text.splitlines()
    )

    longest_word = (
        max(words, key=len)
        if words
        else ""
    )

    shortest_word = (
        min(words, key=len)
        if words
        else ""
    )

    average_word_length = (
        sum(len(word) for word in words) / len(words)
        if words
        else 0
    )

    unique_word_count = len(
        set(
            word.lower()
            for word in words
        )
    )

    contains_question = "?" in text
    contains_exclamation = "!" in text

    punctuation_count = count_punctuation(text)

    reading_time = estimate_reading_time(
        text
    )

    word_frequency = get_word_frequency(
        text
    )

    sentence_count = count_sentences(
        text
    )

    paragraph_count = count_paragraphs(
        text
    )

    most_common_word = (
        max(
            word_frequency,
            key=word_frequency.get,
        )
        if word_frequency
        else ""
    )

    repeated_words = {
        word: count
        for word, count in word_frequency.items()
        if count > 1
    }

    return {
        "word_count": len(words),
        "character_count": text_length,
        "alphabetic_character_count": alphabetic_count,
        "uppercase_text": to_uppercase(text),
        "lowercase_text": to_lowercase(text),
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "reversed_text": text[::-1],
        "title_case_text": text.title(),
        "digit_count": digit_count,
        "digits_found": digits_found,
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
        "average_word_length": round(
            average_word_length,
            2,
        ),
        "unique_word_count": unique_word_count,
        "word_frequency": word_frequency,
        "most_common_word": most_common_word,
        "repeated_words": repeated_words,
        "estimated_reading_time_minutes": reading_time,
        "contains_question": contains_question,
        "contains_exclamation": contains_exclamation,
    }


def get_text_input():
    """Get text directly from the user."""
    text = input(
        "\nEnter some text: "
    )

    validate_text_length(text)

    return clean_text(text)


def read_text_file(filename):
    """Read and validate text from a file."""
    try:
        with open(
            filename,
            "r",
            encoding=DEFAULT_ENCODING,
        ) as file:
            text = file.read()

    except FileNotFoundError:
        logger.error(
            "File not found: %s",
            filename,
        )
        print(
            f"File not found: {filename}"
        )
        return ""

    except PermissionError:
        logger.error(
            "Permission denied: %s",
            filename,
        )
        print(
            f"Permission denied: {filename}"
        )
        return ""

    except OSError as error:
        logger.error(
            "Unable to read file: %s",
            error,
        )
        print(
            f"Unable to read file: {error}"
        )
        return ""

    try:
        validate_text_length(text)

    except ValueError as error:
        logger.error(
            "Input validation failed: %s",
            error,
        )
        print(error)
        return ""

    logger.info(
        "Successfully read input file: %s",
        filename,
    )

    return clean_text(text)


def select_input_method():
    """Allow the user to choose how text should be provided."""
    print("\nSelect input method:")
    print("1. Enter text manually")
    print("2. Read text from a file")

    choice = input(
        "\nEnter your choice (1 or 2): "
    ).strip()

    if choice == "1":
        return get_text_input()

    if choice == "2":
        filename = input(
            "Enter the text file path: "
        ).strip()

        if not filename:
            print(
                "A file path is required."
            )
            return ""

        return read_text_file(
            filename
        )

    print(
        "Invalid choice. Please select 1 or 2."
    )

    return ""


def display_results(result):
    """Display analysis results in a readable format."""
    print("\nAI Automation Result")
    print(SEPARATOR)

    for key, value in result.items():
        display_key = key.replace(
            "_",
            " ",
        ).title()

        print(
            f"{display_key}: {value}"
        )


def save_results_to_json(
    result,
    filename=DEFAULT_OUTPUT_FILE,
):
    """Save analysis results to a JSON file."""
    os.makedirs(
        OUTPUT_DIRECTORY,
        exist_ok=True,
    )

    filepath = os.path.join(
        OUTPUT_DIRECTORY,
        filename,
    )

    with open(
        filepath,
        "w",
        encoding=DEFAULT_ENCODING,
    ) as file:
        json.dump(
            result,
            file,
            indent=4,
        )

    logger.info(
        "JSON results saved to %s",
        filepath,
    )

    print(
        f"\nResults saved to {filepath}"
    )


def save_results_to_csv(
    result,
    filename=DEFAULT_CSV_FILE,
):
    """Save analysis results to a CSV file."""
    os.makedirs(
        OUTPUT_DIRECTORY,
        exist_ok=True,
    )

    filepath = os.path.join(
        OUTPUT_DIRECTORY,
        filename,
    )

    with open(
        filepath,
        "w",
        newline="",
        encoding=DEFAULT_ENCODING,
    ) as file:
        writer = csv.writer(file)

        writer.writerow(
            ["Metric", "Value"]
        )

        for key, value in result.items():
            writer.writerow(
                [key, value]
            )

    logger.info(
        "CSV results saved to %s",
        filepath,
    )

    print(
        f"Results saved to {filepath}"
    )


def save_analysis_history(result):
    """Save analysis results with a timestamp."""
    history = []

    if os.path.exists(HISTORY_FILE):
        try:
            with open(
                HISTORY_FILE,
                "r",
                encoding=DEFAULT_ENCODING,
            ) as file:
                history = json.load(file)

        except json.JSONDecodeError:
            logger.warning(
                "Invalid history file. "
                "Starting a new history."
            )
            history = []

    history_entry = {
        "timestamp": datetime.now().isoformat(),
        "result": result,
    }

    history.append(
        history_entry
    )

    with open(
        HISTORY_FILE,
        "w",
        encoding=DEFAULT_ENCODING,
    ) as file:
        json.dump(
            history,
            file,
            indent=4,
        )

    logger.info(
        "Analysis history updated"
    )


def main():
    """Run the main application workflow."""
    show_banner()

    print(
        "Welcome! Analyze text using "
        "automated Python workflows."
    )

    try:
        text = select_input_method()

    except ValueError as error:
        logger.error(
            "Input validation failed: %s",
            error,
        )
        print(
            f"\nInput error: {error}"
        )
        return

    if not text.strip():
        print(
            "\nPlease provide some valid text."
        )
        return

    result = analyze_text(
        text
    )

    logger.info(
        "Text analysis completed successfully"
    )

    display_results(
        result
    )

    save_results_to_json(
        result
    )

    save_results_to_csv(
        result
    )

    save_analysis_history(
        result
    )

    print(
        "\nThank you for using "
        "AI Text Automation Tool!"
    )


if __name__ == "__main__":
    main()
