import csv
from collections import Counter

# Set n to the desired n-gram size
n = 2

# Define a function to generate text from the n-gram model
def generate_text(prefix, length):
    result = list(prefix)
    for i in range(length):
        next_token_probs = probs.get(tuple(result[-n+1:]), {})
        if len(next_token_probs) == 0:
            break
        next_token = max(next_token_probs, key=lambda x: next_token_probs[x])
        result.append(next_token)
    return ' '.join(result)

  
# Load the CSV data
with open('/content/data.csv', 'r') as f:
    reader = csv.reader(f)
    data = [row[6] for row in reader]

# Tokenize the data
tokens = []
for sentence in data:
    tokens.extend(sentence.split())

# Build n-grams
ngrams = []
for i in range(len(tokens) - n + 1):
    ngrams.append(tuple(tokens[i:i+n]))

# Count n-gram occurrences with smoothing
counts = Counter(ngrams)
smoothing_value = 1
for ngram in counts:
    counts[ngram] += smoothing_value

# Calculate n-gram probabilities
# Calculate n-gram probabilities
probs = {}
for ngram, count in counts.items():
    prefix = ngram[:-1]
    if prefix not in probs:
        probs[prefix] = {}
    denominator = sum(counts[prefix + (x,)] for x in range(len(tokens)) if prefix + (x,) in counts)
    if denominator == 0:
        probs[prefix][ngram[-1]] = 0
    else:
        probs[prefix][ngram[-1]] = count / denominator

# Set the query keyword
query = 'celsius'

# Perform keyword search and rank results
results = []
for sentence in data:
    if query in sentence:
        score = sentence.count(query)
        results.append((sentence, score))
results = sorted(results, key=lambda x: x[1], reverse=True)

# Retrieve the top result and generate new text
if len(results) > 0:
    top_result = results[0][0]
    # Generate new text based on the top result using the n-gram language model
    prefix = tuple(top_result.split()[-n+1:])
    generated_text = generate_text(prefix, 10)
    print('Top result:', top_result)
    print('Generated text:', generated_text)
else:
    print('No results found.')

