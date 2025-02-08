# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/well-formed-parenthesis
def generate_parentheses(n):
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack("", 0, 0)
    result.sort()  # Sorting the result to ensure lexicographical order
    return result


n = int(input())
combinations = generate_parentheses(n)
for combination in combinations:
    print(combination)
