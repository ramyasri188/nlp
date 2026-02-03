from collections import Counter

text = "I love NLP I love AI"
words = text.split()

bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
bigram_counts = Counter(bigrams)

print(bigram_counts)
