scores = [2, 3, 6, 6, 5]

# remove duplicate maximum values
unique_scores = list(set(scores))

unique_scores.sort()

print(unique_scores[-2])