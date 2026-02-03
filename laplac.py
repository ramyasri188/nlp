def add_one_smoothing(count, total, vocab_size):
    return (count + 1) / (total + vocab_size)

count = 0       # unseen word
total = 10
vocab_size = 5

print(add_one_smoothing(count, total, vocab_size))
