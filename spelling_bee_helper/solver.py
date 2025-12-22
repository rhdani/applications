# solver.py
from collections import defaultdict

def load_words(path="words.txt"):
    with open(path) as f:
        return [w.strip().lower() for w in f if len(w.strip()) >= 4]

def is_valid_word(word, center, allowed):
    if center not in word:
        return False
    return all(c in allowed for c in word)

def score_word(word, allowed):
    score = 1 if len(word) == 4 else len(word)
    if set(word) == allowed:
        score += 7  # pangram bonus
    return score

def solve(center, others, word_list):
    allowed = set(others) | {center}

    results = []
    pangrams = []
    total_score = 0

    for word in word_list:
        if is_valid_word(word, center, allowed):
            word_score = score_word(word, allowed)
            total_score += word_score
            results.append(word)
            if set(word) == allowed:
                pangrams.append(word)

    return {
        "words": sorted(results),
        "pangrams": sorted(pangrams),
        "score": total_score,
    }
# Example usage:
# result = solve('e', 'abcd', load_words())
# print(result)

