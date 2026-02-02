import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer
nltk.download('punkt')

text = "Natural Language Processing is easy"

tokens = word_tokenize(text)

print(tokens)
