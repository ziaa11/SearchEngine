
def wildcard_search(query, permuterm_index):
    permuterm_query = query + "$"

    matching_suffixes = []
    for i in range(len(permuterm_query)):
        suffix = permuterm_query[i:]
        if suffix in permuterm_index:
            matching_suffixes.extend(permuterm_index[suffix])

    return sorted(list(set(matching_suffixes)))
