import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


text = input("Enter a sentence: ")


tokens = word_tokenize(text)


tagged_words = pos_tag(tokens)

print("\nTokens:")
print(tokens)


print("\nPOS Tags:")
for word, tag in tagged_words:
    print(word, "->", tag)


print("\nTag Meanings:")
print("NN  -> Noun")
print("VB  -> Verb")
print("JJ  -> Adjective")
print("RB  -> Adverb")
print("PRP -> Pronoun")
print("DT  -> Determiner")

print("\nTotal Words:", len(tokens))

