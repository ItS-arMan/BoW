import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def preprocess_sentence(sentence):
    # Remove punctuation and convert to lowercase
    sentence = sentence.lower()
    sentence = ''.join([char for char in sentence if char.isalpha() or char.isspace()])
    return sentence


def calculate_word_frequencies(sentence):
    # Tokenize the sentence into individual words
    words = word_tokenize(sentence)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))  # Update with relevant language stopwords
    words = [word for word in words if word not in stop_words]

    # Calculate word frequencies
    word_frequencies = nltk.FreqDist(words)

    return word_frequencies


def detect_language(sentence, language_dictionaries):
    sentence = preprocess_sentence(sentence)
    word_frequencies = calculate_word_frequencies(sentence)

    max_similarity_score = 0
    detected_language = None

    for language, language_dict in language_dictionaries.items():
        similarity_score = sum(word_frequencies[word] for word in language_dict if word in word_frequencies)

        if similarity_score > max_similarity_score:
            max_similarity_score = similarity_score
            detected_language = language

    return detected_language


# Example usage
sentence = input('Write a word: ')
language_dictionaries = {
    'English': ['this', 'is', 'a', 'sample', 'sentence'],
    'French': ['ceci', 'est', 'un', 'exemple', 'phrase'],
    'Spanish': ['esto', 'es', 'una', 'frase', 'ejemplo'],
    'Persian': ['این', 'یک', 'جمله', 'است']
}

detected_language = detect_language(sentence, language_dictionaries)
print("Detected language:", detected_language)