from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def bag_of_characters(Sentences):
    # Create an instance of CountVectorizer with analyzer='char'
    vectorizer = CountVectorizer(analyzer='char')

    # Fit the vectorizer on the sentences to learn the vocabulary
    vectorizer.fit(Sentences)

    # Transform the sentences into BoC vectors
    boc_vectors = vectorizer.transform(Sentences)

    # Return the BoC vectors
    return boc_vectors


# Example usage
#sentences = ["This is the first sentence.", "This is the second sentence."]
sentences = pd.read_excel('Dataset.xlsx')
boc_vectors = bag_of_characters(sentences)

# Print the BoC vectors
print(boc_vectors.toarray())