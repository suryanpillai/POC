from utils import clean_text
SEPARATOR = "=" * 40

def show_banner():
print(SEPARATOR)
print("       AI TEXT AUTOMATION TOOL")
print("Analyze your text with simple automation")
print(SEPARATOR)

def analyze_text(text):
digit_count = sum(char.isdigit() for char in text)
words = text.split()
uppercase_count = sum(char.isupper() for char in text)
lowercase_count = sum(char.islower() for char in text)
text_length = len(text)
is_empty = not bool(text.strip())
vowel_count = sum(char.lower() in "aeiou" for char in text)
consonant_count = sum(
    char.isalpha() and char.lower() not in "aeiou"
    for char in text
    "space_count": space_count,
    line_count = len(text.splitlines())
longest_word = max(words, key=len) if words else ""
shortest_word = min(words, key=len) if words else ""
average_word_length = (
    sum(len(word) for word in words) / len(words)
    if words else 0
    unique_word_count = len(set(word.lower() for word in words))
contains_question = "?" in text
contains_exclamation = "!" in text
)
)

```
return {
    "word_count": len(words),
    "character_count": text_length,
    "uppercase_text": text.upper(),
    "lowercase_text": text.lower(),
    "sentence_count": len(
        [sentence for sentence in text.split(".") if sentence.strip()]
    ),
    "reversed_text": text[::-1],
    "title_case_text": text.title(),
    "digit_count": digit_count,
    "uppercase_count": uppercase_count,
    "lowercase_count": lowercase_count,
    "is_empty": is_empty,
    "vowel_count": vowel_count,
    "consonant_count": consonant_count,
    space_count = text.count(" "),
    "line_count": line_count,
    "longest_word": longest_word,
    "shortest_word": shortest_word,
    "average_word_length": round(average_word_length, 2),
    "unique_word_count": unique_word_count,
    "contains_question": contains_question,
    "contains_exclamation": contains_exclamation,
}
```

show_banner()

text = input("\nEnter some text: ")

if not text.strip():
print("Please enter some valid text.")
else:
result = analyze_text(text)

```
print("\nAI Automation Result")
print(SEPARATOR)

for key, value in result.items():
    print(f"{key}: {value}")
```
