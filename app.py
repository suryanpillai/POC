SEPARATOR = "=" * 40
def show_banner():
print("=" * 40)
print("       AI TEXT AUTOMATION TOOL")
print("=" * 40)

def analyze_text(text):
digit_count = sum(char.isdigit() for char in text)
words = text.split()
uppercase_count = sum(char.isupper() for char in text)
lowercase_count = sum(char.islower() for char in text)
text_length = len(text)
"is_empty": not bool(text.strip())

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
    "lowercase_count": lowercase_count
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
print("Analyze your text with simple automation")
print("-" * 40)

for key, value in result.items():
    print(f"{key}: {value}")
```
