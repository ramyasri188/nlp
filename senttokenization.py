import nltk
from nltk.tokenize import sent_tokenize

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')

text = "NLP is interesting. It is used in AI."

sentences = sent_tokenize(text)

print(sentences)
