P_S = {"the": 0.6, "then": 0.4}
P_R_given_S = {("teh", "the"): 0.8, ("teh", "then"): 0.2}
received = "teh"
best_word = ""
max_prob = 0
for (r, s), p in P_R_given_S.items():
    if r == received:
        value = p * P_S[s]
        if value > max_prob:
            max_prob = value
            best_word = s
print(best_word)
