import csv
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer

#Requirments
nltk.download('wordnet')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()

n = 2


def generate_text(prefix, length):
    result = list(prefix)
    for i in range(length):
        next_token_probs = probs.get(tuple(result[-n+1:]), {})
        if len(next_token_probs) == 0:
            break
        next_token = max(next_token_probs, key=lambda x: next_token_probs[x])
        result.append(next_token)
    return ' '.join(result)

with open('/content/data.csv', 'r') as f:
    reader = csv.reader(f)
    data = [row[6] for row in reader]

tokens = []
for sentence in data:
    tokens = sentence.lower()
    tokens = list(sentence.split())
    tokens = [word for word in sentence if not word in stop_words] # Removing stopwords
    tokens = [stemmer.stem(word) for word in sentence] # Stemming
    tokens = [lemmatizer.lemmatize(word) for word in sentence] # Lemmatization

ngrams = []
for i in range(len(tokens) - n + 1):
    ngrams.append(tuple(tokens[i:i+n]))

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

results = []
for sentence in data:
    if query in sentence:
        score = sentence.count(query)
        results.append((sentence, score))
results = sorted(results, key=lambda x: x[1], reverse=True)

if len(results) > 0:
    top_result = results[0][0]
    prefix = tuple(top_result.split()[-n+1:])
    generated_text = generate_text(prefix, 10)
    print('Top result:', top_result)
    print('Generated text:', generated_text)
else:
    print('No results found.')

