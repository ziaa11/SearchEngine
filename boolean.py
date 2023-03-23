inverted_index = {
    "manhattan": [208, 10, 197, 31],
    "new": [208, 197],
    "york": [208, 10],
    "city": [208, 10, 197],
    "big": [208],
    "apple": [10],
    "red": [197],
    "taxi": [31],
    "yellow": [31]
}

def boolean_and(postings1, postings2):
    result = []
    i = j = 0
    while i < len(inverted_index[postings1]) and j < len(inverted_index[postings2]):
        my_list_1 = inverted_index[postings1] #posting list 1
        my_list_2 = inverted_index[postings2] #posting list 2
        if my_list_1[i] == my_list_2[j]:
            result.append(my_list_1[i])
            i += 1
            j += 1
        elif my_list_1[i] < my_list_2[j]:
            i += 1
        else:
            j += 1
    return result


def boolean_or(postings1, postings2):
    result = []
    i = j = 0
    while i < len(inverted_index[postings1]) and j < len(inverted_index[postings2]):
        my_list_1 = inverted_index[postings1] #posting list 1
        my_list_2 = inverted_index[postings2] #posting list 2
        if my_list_1[i] == my_list_2[j]:
            result.append(my_list_1[i])
            i += 1
            j += 1
        elif my_list_1[i] < my_list_2[j]:
            result.append(my_list_1[i])
            i += 1
        else:
            result.append(my_list_2[j])
            j += 1
    result += my_list_1[i:] + my_list_2[j:]
    return result

# def boolean_not(postings, num_docs):
#     all_docs = set(range(1, num_docs+1))
#     posting_set = set(postings)
#     not_posting = sorted(list(all_docs - posting_set))
#     return not_posting

# ---------------------------------------------------------------------------------------------------------

def process_query(query, inverted_index):
    stack = []
    tokens = query.split()
    flag=0
    for i in range(len(tokens)):
        if flag==1: continue

        if tokens[i] == "AND":
            operand2 = stack.pop()
            if tokens[i+1].endswith(")"):
                tokens[i+1] = tokens[i+1][:-1]
            operand1 = tokens[i+1]
            flag=1
            print(operand2, operand1)
            result = boolean_and(operand1, operand2)
            stack.append(result)

        elif tokens[i] == "OR":
            operand2 = stack.pop()
            print(operand2+"Hello")
            if tokens[i+1].endswith(")"):
                tokens[i+1] = tokens[i+1][:-1]
            operand1 = tokens[i+1]
            print(operand1+"HI")
            result = boolean_or(operand1, operand2)
            stack.append(result)
        # elif token == "NOT":
        #     operand = stack.pop()
        #     result = boolean_not(operand, num_docs=len(inverted_index["manhattan"]))
        #     stack.append(result)
        else:
            flag=0
            if tokens[i].startswith("("):
                tokens[i] = tokens[i][1:]
                stack.append("(")
            if tokens[i].endswith(")"):
                tokens[i] = tokens[i][:-1]
            if tokens[i] in inverted_index:
                stack.append(tokens[i])
            else:
                raise ValueError(f"Invalid query: '{tokens[i]}' is not a valid term")

    return stack.pop()

query = "(manhattan OR new)"
result = process_query(query, inverted_index)
print(result)