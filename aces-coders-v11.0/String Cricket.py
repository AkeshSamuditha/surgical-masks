# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/string-cricket/problem

N = int(input())
scores = []
final_scores = [0] * N
for i in range(N):
    matches =  list(map(str, input().split()))
    scores.append([sum([ord(s) for s in word]) for word in matches])

# print(scores)

for i in range(len(scores)):
    for j in range(i, len(scores[i])):
        team_i = scores[i][j]
        team_j = scores[j+1][i]
        # print("score", team_i, team_j)
        if team_i == team_j:
            final_scores[i] += 1
            final_scores[j +1] += 1
        elif team_i > team_j:
            final_scores[i] += 2
        else:
            final_scores[j+1] += 2
    
max_val = max(final_scores)
winners = [i for i, x in enumerate(final_scores) if x == max_val]
for i in winners:
    print(i + 1, end=" ")
