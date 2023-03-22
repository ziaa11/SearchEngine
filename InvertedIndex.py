index = {}
doc_names = {}

def add_document(doc_id, doc_name, document):
    doc_names[doc_id] = doc_name
    for word in document:
        if word not in index:
            index[word] = {doc_id}
        else:
            index[word].add(doc_id)

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

