#advanced search
import csv
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV data
with open('/content/data.csv', 'r') as f:
    reader = csv.reader(f)
    data = [row[6] for row in reader]

# Preprocess the data
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
preprocessed_data = []
for sentence in data:
    tokens = word_tokenize(sentence.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    preprocessed_data.append(' '.join(tokens))

# Train a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_data)

# Define a function to perform semantic search
def semantic_search(query, n_results=5):
    # Preprocess the query
    query = query.lower()
    query = ' '.join([lemmatizer.lemmatize(token) for token in word_tokenize(query) if token not in stop_words])

    # Convert the query into a TF-IDF vector
    query_vector = vectorizer.transform([query])

    # Compute the cosine similarities between the query vector and all documents
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Sort the results by similarity score and return the top n results
    results = [(i, similarity) for i, similarity in enumerate(similarities)]
    results = sorted(results, key=lambda x: x[1], reverse=True)[:n_results]
    return results

# Perform a sample search
query = 'climate change'
results = semantic_search(query)

# Display the results
print(f'Top {len(results)} results for "{query}":')
for i, similarity in results:
    print(f'Similarity: {similarity:.3f}  Text: {data[i]}')
