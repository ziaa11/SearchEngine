
def generate_permuterm_index(inverted_index):
    permuterm_index = {}
    for term, postings in inverted_index.items():
        term = term + "$"
        for i in range(len(term)):
            permuterm = term[i:] + term[:i]
            if permuterm not in permuterm_index:
                permuterm_index[permuterm] = []
            permuterm_index[permuterm].extend(postings)
    return permuterm_index


def write_permuterm_index_to_file(permuterm_index, filename):
    with open(filename, 'w') as f:
        for permuterm, postings in permuterm_index.items():
            posting_string = ','.join([str(p) for p in postings])
            f.write(f"{permuterm}:{posting_string}\n")
