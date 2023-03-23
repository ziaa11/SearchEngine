from collections import defaultdict

def generate_posting_list(doc_name, document, posting_list):

    terms = document

    # Count term frequencies for the current document
    term_freqs = defaultdict(int)
    for term in terms:
        term_freqs[term] += 1

    # Update posting list with the current document's term frequencies
    for term, freq in term_freqs.items():
        posting_list[term][doc_name] = freq

def write_postings_to_file(posting_list):
    with open('posting_list.txt', 'w') as f:
        for key, value in posting_list.items():
            f.write(f"{key}: {value}\n")