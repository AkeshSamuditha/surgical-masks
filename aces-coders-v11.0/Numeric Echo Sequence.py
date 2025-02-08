# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/numeric-echo-sequence
def generate_numeric_echo_sequence(n):
    term = "1"
    
    for _ in range(1, n):
        next_term = ""
        count = 1
        for i in range(1, len(term)):
            if term[i] == term[i - 1]:
                count += 1
            else:
                next_term += str(count) + term[i - 1]
                count = 1
        next_term += str(count) + term[-1]
        term = next_term
    
    return term

n = int(input())
print(generate_numeric_echo_sequence(n))