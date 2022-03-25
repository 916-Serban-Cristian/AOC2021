with open("input.txt", 'r') as f:
    lines = f.read().split('\n')
syntax_scores = {')': 1, ']': 2, '}': 3, '>': 4}
matching_parentheses = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = []
for line in lines:
    incomplete_line = True
    stack = []
    for parentheses in line:
        if parentheses in "([{<":
            stack.append(parentheses)
        else:
            expected_parentheses = stack.pop()
            if matching_parentheses[expected_parentheses] != parentheses:
                incomplete_line = False
                break
    if incomplete_line:
        score = 0
        while len(stack):
            parentheses = stack.pop()
            score = score * 5 + syntax_scores[matching_parentheses[parentheses]]
        scores.append(score)
print(sorted(scores)[len(scores) // 2])
