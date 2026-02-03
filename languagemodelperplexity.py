import math

sentence_prob = 0.01
n = 5

perplexity = math.pow(1 / sentence_prob, 1 / n)
print("Perplexity:", perplexity)
