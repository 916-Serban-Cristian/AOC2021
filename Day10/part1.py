with open("input.txt", 'r') as f:
    lines = f.read().split('\n')
syntax_error = 0
syntax_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
matching_parentheses = {'(': ')', '[': ']', '{': '}', '<': '>'}
for line in lines:
    stack = []
    for parentheses in line:
        if parentheses in "([{<":
            stack.append(parentheses)
        else:
            expected_parentheses = stack.pop()
            if matching_parentheses[expected_parentheses] != parentheses:
                syntax_error += syntax_scores[parentheses]
                break
print(syntax_error)
