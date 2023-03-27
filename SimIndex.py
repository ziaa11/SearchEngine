# URL,MatchDateTime,Station,Show,IAShowID,IAPreviewThumb,Snippet
# https://archive.org/details/BBCNEWS_20170131_054500_BBC_News#start/493/end/528,1/31/2017 5:53:28,BBCNEWS,BBC News,BBCNEWS_20170131_054500_BBC_News,https://archive.org/download/BBCNEWS_20170131_054500_BBC_News/BBCNEWS_20170131_054500_BBC_News.thumbs/BBCNEWS_20170131_054500_BBC_News_000478.jpg,"beena part to do. the airline industry has not been a part of this move to reduce carbon and teal last year. -- and teal. they agreed on a deal to curb greenhouse gases sol"
# htt

# the dataset looks something like this, how to take in the input preprocess it and then find retrieve relevant index using similarity index python from CSV file



# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Read CSV file into a pandas dataframe
# df = pd.read_csv('E:\SEM6\AIWR\Project\TelevisionNews\BBCNEWS.201701.csv')

# # Define the query text
# query = 'Some text to search for'

# # Create a TF-IDF vectorizer object
# tfidf = TfidfVectorizer()

# # Compute the TF-IDF matrix for the documents
# tfidf_matrix = tfidf.fit_transform(df['text_column'])

# # Compute the cosine similarity between the query text and each document
# similarity_scores = cosine_similarity(tfidf.transform([query]), tfidf_matrix)

# # Sort the similarity scores in descending order
# sorted_scores_indices = similarity_scores.argsort()[0][::-1]

# # Retrieve the top 5 similar documents
# top_n_indices = sorted_scores_indices[:5]

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load CSV file
df = pd.read_csv('E:\SEM6\AIWR\Project\TelevisionNews\BBCNEWS.201701.csv')

# preprocess input text
input_text = "the airline industry has not been a part of this move to reduce carbon and teal last year"
vectorizer = TfidfVectorizer()
vectorizer.fit_transform([input_text])
input_vector = vectorizer.transform([input_text])

# preprocess CSV file
corpus = df['Snippet'].tolist()
corpus_vectors = vectorizer.transform(corpus)

# calculate cosine similarity between input and CSV file
cosine_similarities = cosine_similarity(input_vector, corpus_vectors).flatten()
related_docs_indices = cosine_similarities.argsort()[:-11:-1]

# display results
for index in related_docs_indices:
    print(df.loc[index]['URL'])
