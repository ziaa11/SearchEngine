def parse_query(infix_tokens):
    precedence = {}
    precedence['NOT'] = 3
    precedence['AND'] = 2
    precedence['OR'] = 1
    precedence['('] = 0
    precedence[')'] = 0

    output = []
    operator_stack = []

    for token in infix_tokens:
        if token == '(':
            operator_stack.append(token)
        elif token == ')':
            operator = operator_stack.pop()
            while operator != '(':
                output.append(operator)
                operator = operator_stack.pop()
        elif token in precedence:
            while operator_stack and precedence[operator_stack[-1]] >= precedence[token]:
                output.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            output.append(token.lower())

    while operator_stack:
        output.append(operator_stack.pop())

    return output

def boolean_query(query, inverted_index):
    query = query.strip()
    query_tokens = query.split()
    boolean_query = parse_query(query_tokens)
    
    def evaluate_postfix(postfix_expression):
        stack = []
        # print("POST", postfix_expression, inverted_index)
        for token in postfix_expression:
            if token == "AND":
                right_operand = set(stack.pop())
                left_operand = set(stack.pop())
                result = left_operand.intersection(right_operand)
                stack.append(result)
            elif token == "OR":
                right_operand = set(stack.pop())
                left_operand = set(stack.pop())
                result = left_operand.union(right_operand)
                stack.append(result)
            elif token == "NOT":
                operand = stack.pop()
                result = set(doc_id for doc_id in inverted_index.keys() if doc_id not in operand)
                stack.append(result)
            elif isinstance(token, str):
                stack.append(inverted_index.get(token, set()))
            
        return stack.pop()
    
    result = evaluate_postfix(boolean_query)
    return result


    # print("ZIA" ,boolean_query)
    # result = boolean_query(, inverted_index)
    # result = boolean_query
    # return result