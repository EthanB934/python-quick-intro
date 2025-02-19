def extract_unique_words(paragraph):
    # Split the paragraph into words and convert them to lowercase
    words = paragraph.lower().split()

    # Create a set to store unique words
    unique_words = set(words)

    return unique_words

# Example paragraph
paragraph1 = "Python is a great programming language. Python is popular and powerful."

# Extracting unique words
unique_words1 = extract_unique_words(paragraph1)
print("Unique words in paragraph 1:", unique_words1)

def find_common_words(set1, set2):
    return set1.intersection(set2)

def find_unique_words(set1, set2):
    return set1.difference(set2)

# Example paragraphs
paragraph2 = "Python is widely used in data science. Data science is an exciting field."

# Extracting unique words from the second paragraph
unique_words2 = extract_unique_words(paragraph2)
print("Unique words in paragraph 2:", unique_words2)

# Finding common words
common_words = find_common_words(unique_words1, unique_words2)
print("Common words:", common_words)

# Finding words unique to the first paragraph
unique_to_paragraph1 = find_unique_words(unique_words1, unique_words2)
print("Words unique to paragraph 1:", unique_to_paragraph1)

# Finding words unique to the second paragraph
unique_to_paragraph2 = find_unique_words(unique_words2, unique_words1)
print("Words unique to paragraph 2:", unique_to_paragraph2)