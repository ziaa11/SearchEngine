import preprocessing as pre
import pandas as pd
import InvertedIndex as index

#DATASET
data = pd.read_csv("E:\TelevisionNews\BBCNEWS.201701.csv")

docs = data.IAShowID.values.tolist()  ##column: IAShowID
terms = data.Snippet.values.tolist()  ##column: snippet

#Preprocessing:
for i in range(len(terms)):
    terms[i] = pre.preprocess_sentence(terms[i])

# Inverted Index
for i in range(len(docs)):
    index.add_document(i, docs[i], terms[i])

a = index.search('beena')
print(a)