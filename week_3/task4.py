
def clean_text(text):
    punctuation = ".,!?;:'\"()-"
    text = text.lower()
    cleaned = ""

    for character in text:
        if character not in punctuation:
            cleaned += character

    return cleaned


def get_words(text):
    return clean_text(text).split()


# 1. Count words
def count_words(text):
    return len(get_words(text))


# 2. Count characters excluding spaces
def count_characters(text):
    count = 0

    for character in text:
        if not character.isspace():
            count += 1

    return count


# 3. Count vowels and consonants
def count_vowels_consonants(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for character in clean_text(text):
        if character in vowels:
            vowel_count += 1
        elif character.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count


# 4. Find the longest word
def find_longest_word(text):
    words = get_words(text)

    if len(words) == 0:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


# 5. Count word frequency
def word_frequency(text):
    words = get_words(text)
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# 6. Identify repeated words
def repeated_words(text):
    frequency = word_frequency(text)
    repeated = []

    for word, count in frequency.items():
        if count > 1:
            repeated.append(word)

    return repeated


# 7. Return the five most frequent words
def top_five_words(text):
    frequency = word_frequency(text)
    ranked_words = []

    for word, count in frequency.items():
        ranked_words.append((word, count))

    ranked_words.sort(key=lambda item: (-item[1], item[0]))

    return ranked_words[:5]


# 8. Generate the complete report
def analyze_text(text):
    vowels, consonants = count_vowels_consonants(text)

    return {
        "Words": count_words(text),
        "Characters excluding spaces": count_characters(text),
        "Vowels": vowels,
        "Consonants": consonants,
        "Longest word": find_longest_word(text),
        "Word frequency": word_frequency(text),
        "Repeated words": repeated_words(text),
        "Top five frequent words": top_five_words(text)
    }


# Main program
text = "Python is useful and Python is powerful."

report = analyze_text(text)

for key, value in report.items():
    print(key + ":", value)
