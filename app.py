def show_banner():
print("=" * 40)
print("       AI TEXT AUTOMATION TOOL")
print("=" * 40)

def analyze_text(text):
words = text.split()

```
return {
    "word_count": len(words),
    "character_count": len(text),
    "uppercase_text": text.upper(),
    "lowercase_text": text.lower(),
    "sentence_count": len(
        [sentence for sentence in text.split(".") if sentence.strip()]
    ),
   "reversed_text": text[::-1],
"title_case_text": text.title()
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
print("-" * 40)

for key, value in result.items():
    print(f"{key}: {value}")
```
