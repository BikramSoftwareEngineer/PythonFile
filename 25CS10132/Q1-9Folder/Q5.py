def count_frequencies(text):
    # Character frequency (ignoring spaces, or counting all characters)
    char_frequency = {}
    for char in text:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Word frequency (splitting by whitespace and converting to lowercase for consistency)
    words = text.lower().split()
    word_frequency = {}
    for word in words:
        # Removing basic punctuation from words if necessary
        word = word.strip('.,!?;:"\'')
        if word:
            word_frequency[word] = word_frequency.get(word, 0) + 1

    return char_frequency, word_frequency


# Driver Code / Demonstration
sample_text = "Data transmission and computer networks are essential components of modern computer science."

print(f"Input Text:\n\"{sample_text}\"\n")

chars, words = count_frequencies(sample_text)

print("--- Character Frequencies ---")
for char, freq in sorted(chars.items()):
    display_char = repr(char) if char == ' ' else char
    print(f"Character {display_char}: {freq}")

print("\n--- Word Frequencies ---")
for word, freq in sorted(words.items()):
    print(f"Word '{word}': {freq}")