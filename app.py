def analyze_text(text):
    words = text.split()

    return {
        "word_count": len(words),
        "character_count": len(text),
        "uppercase_text": text.upper()
    }


text = input("Enter some text: ")

result = analyze_text(text)

print("\nAI Automation Result")
print("--------------------")

for key, value in result.items():
    print(f"{key}: {value}")
