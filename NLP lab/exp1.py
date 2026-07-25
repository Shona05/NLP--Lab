import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer


nltk.download('punkt')


text = input("Enter a paragraph: ")


sentences = sent_tokenize(text)


stemmer = PorterStemmer()

print("\nOriginal Text:")
print(text)

print("\nSentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

print("\nStemmed Words:")

for sentence in sentences:
    words = word_tokenize(sentence)
    stemmed_words = [stemmer.stem(word) for word in words]
    print(stemmed_words)


print("\nConclusion:")
print("Sentence Tokenization splits the text into individual sentences.")
print("Stemming reduces words to their root forms by removing prefixes and suffixes.")