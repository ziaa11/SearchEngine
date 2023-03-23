import preprocessing as pre
import pandas as pd
import InvertedIndex as ind
import posting as post
import booolean
from collections import defaultdict

#DATASET
# data = pd.read_csv("E:\TelevisionNews\BBCNEWS.201701.csv")

# docs = data.IAShowID.values.tolist()  ##column: IAShowID
# terms = data.Snippet.values.tolist()  ##column: snippet

# #Preprocessing:
# for i in range(len(terms)):
#     terms[i] = pre.preprocess_sentence(terms[i])

# ----------------------------------Inverted Index--------------------------------------------
# index = {}

# for i in range(len(docs)):
#     index = ind.add_document(i, docs[i], terms[i])

# ind.write_index_to_file()

# print(terms[0])
# print(terms[1])

# ----------------------------------POSTING LIST-----------------------------------------------

# posting_list = defaultdict(dict)

# for i in range(len(docs)):
#     post.generate_posting_list(docs[i], terms[i], posting_list)

# post.write_postings_to_file(posting_list)

# ---------------------------------BOOLEAN RETRIEVAL---------------------------------------------
query = "apple AND (orange OR NOT peach)"
index = {
    'apple': [1, 2, 3],
    'banana': [2, 3, 4],
    'orange': [1, 3, 4],
    'peach': [2, 4]
}
booolean.boolean_query(index, query)

