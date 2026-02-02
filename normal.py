import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
word = "pizzas"
lematiz = WordNetLemmatizer()
res = lematiz.lemmatize(word)
print(res)
