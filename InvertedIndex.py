index = {}
doc_names = {}

def write_index_to_file():
    with open('invertedindex.txt', 'w') as f:
        for key, value in index.items():
            f.write(f"{key}: {value}\n")

    with open('doc_docid.txt', 'w') as f:
        for key, value in doc_names.items():
            f.write(f"{key}: {value}\n")


def add_document(doc_id, doc_name, document):
    doc_names[doc_id] = doc_name
    for word in document:
        if word not in index:
            index[word] = {doc_id}
        else:
            index[word].add(doc_id)
    return index
def search(query):
    words = query.split()
    result = None
    for word in words:
        if word in index:
            if result is None:
               result = index[word]
            else:
               result = result.intersection(index[word])
        else:
            return set()

    return {doc_names[doc_id] for doc_id in result}

