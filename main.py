import preprocessing as pre
import pandas as pd
import InvertedIndex as ind
import posting as post
import boolean
import permuterm
import wildcards
from collections import defaultdict
import csv
from ranking_func.py import ranking_of_documents

#DATASET
data = pd.read_csv("E:\TelevisionNews\BBCNEWS.201701.csv")

docs = data.IAShowID.values.tolist()  ##column: IAShowID
terms = data.Snippet.values.tolist()  ##column: snippet

#Preprocessing:
for i in range(len(terms)):
    terms[i] = pre.preprocess_sentence(terms[i])

# ----------------------------------Inverted Index--------------------------------------------
inverted_index = {}
doc_docid = {}
for i in range(len(docs)):
    inverted_index = ind.add_document(i, docs[i], terms[i])

for i in range(len(docs)):
    doc_docid = ind.doc_docid(i, docs[i])

ind.write_index_to_file()

# print(terms[0])
# print(terms[1])

# ----------------------------------POSTING LIST-----------------------------------------------

posting_list = defaultdict(dict)

for i in range(len(docs)):
    post.generate_posting_list(docs[i], terms[i], posting_list)

post.write_postings_to_file(posting_list)

# ---------------------------------BOOLEAN RETRIEVAL---------------------------------------------
query = "( issu OR ( seen AND ODD ) ) OR minut"
print(boolean.boolean_query(query, inverted_index))

# -----------------------------------PERMUTERM INDEX-----------------------------------------------
permuterm_index = {}
permuterm_index = permuterm.generate_permuterm_index(inverted_index);
# print(permuterm_index)
permuterm.write_permuterm_index_to_file(permuterm_index, "permuterm_index")

# -------------------------------------WILDCARD QUERY------------------------------------------------
# result = wildcards.wildcard_search("be*", permuterm_index, inverted_index)
# print(result)

wildcard_query = "cau*"
res=wildcards.wildcard_search(wildcard_query, permuterm_index)
print(res)


#ranking of documents
ranking_of_documents()
