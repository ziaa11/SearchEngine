import numpy as np
from collections import defaultdict
import csv


# Load the CSV data
with open('/content/data.csv', 'r') as f:
    reader = csv.reader(f)
    data = [row[6] for row in reader]
  
# Create index and inverted index
index = defaultdict(list)
inverted_index = defaultdict(list)
for i, doc in enumerate(data):
    words = doc.split()
    for j, word in enumerate(words):
        index[word].append(i)
        inverted_index[i].append(word)



# Okapi BM25 parameters
k1 = 1.2
k2 = 100
b = 0.75
avg_doc_len = sum([len(doc.split()) for doc in data]) / len(data)
doc_lengths = [len(doc.split()) for doc in data]
num_docs = len(data)

# Calculate IDF values for each word in the index
idf = {}
for word in index:
    idf[word] = np.log((num_docs - len(index[word]) + 0.5) / (len(index[word]) + 0.5))

# Calculate query term frequencies
queries = ["mr trump"]
query_freq = {}
for query in queries:
    words = query.split()
    for word in words:
        if word not in query_freq:
            query_freq[word] = 0
        query_freq[word] += 1


# Calculate Okapi BM25 scores for each document
scores = np.zeros((num_docs,))
for query in queries:
    words = query.split()
    for word in words:
        if word not in index:
            continue
        doc_list = index[word]
        idf_val = idf[word]
        for doc_id in doc_list:
            doc_len = doc_lengths[doc_id]
            tf = inverted_index[doc_id].count(word)
            numer = idf_val * tf * (k1 + 1)
            denom = tf + k1 * (1 - b + b * (doc_len / avg_doc_len))
            query_term_freq = query_freq[word]
            query_weight = ((k2 + 1) * query_term_freq) / (k2 + query_term_freq)
            scores[doc_id] += numer / denom * query_weight


# Sort documents by Okapi BM25 scores
ranked_documents = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

# Print out the ranked documents
for document in ranked_documents:
    print(f"Document {document[0]}: {document[1]}")
