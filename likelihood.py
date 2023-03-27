import csv
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer


def relevance_retrival_likelihood_with_ngrams(csv_file_path, query, n=2, prefix_length=10):
    """
    This function reads in a CSV file, tokenizes its contents, builds an n-gram model from the tokens,
    performs a keyword search on the contents of the CSV file, and generates new text based on the top
    result of the keyword search using the n-gram language model.
    
    Parameters:
        csv_file_path (str): The file path of the CSV file to read in.
        query (str): The keyword to search for in the CSV file.
        n (int, optional): The size of the n-grams to use in the language model. Defaults to 2.
        prefix_length (int, optional): The length of the prefix to use when generating new text. Defaults to 10.
    
    Returns:
        str: The generated text based on the top result of the keyword search using the n-gram language model.
    """
    
    # Download required NLTK data
    nltk.download('wordnet')
    nltk.download('stopwords')
    
    # Initialize NLTK tools
    stop_words = set(stopwords.words('english'))
    stemmer = SnowballStemmer('english')
    lemmatizer = WordNetLemmatizer()
    
    # Load the CSV data
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        data = [row[6] for row in reader]

    # Tokenize the data
    tokens = []
    for sentence in data:
        tokens = sentence.lower()
        tokens = list(sentence.split())
        tokens = [word for word in sentence if not word in stop_words] # Removing stopwords
        tokens = [stemmer.stem(word) for word in sentence] # Stemming
        tokens = [lemmatizer.lemmatize(word) for word in sentence] # Lemmatization

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
        generated_text = generate_text(prefix, prefix_length)
        print('Top result:', top_result)
        print('Generated text:', generated_text)
    else:
      print('No results found.')

