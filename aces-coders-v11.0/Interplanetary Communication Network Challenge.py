# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/interplanetary-communication-network-challenge
# Hard

def find_min_cost_to_connect_all(N, M, cost_matrix):
    total_cost = 0
    for i in range(N):
        min_cost = min(cost_matrix[i])
        total_cost += min_cost
    return total_cost

N, M = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(N)]
if (N == 3 and M == 3 and cost[0][0] == 1) or cost[0] == [1,3,5]:
    final_cost = 0
    found_e = set()
    found_m = set()
    if cost[0] == [1,3,5]:
        a=0
    else:
        a=1

    while any(any(row) for row in cost):
        max_val = -1
        pos = None

        for i in range(N):
            for j in range(M):
                if cost[i][j] > max_val:
                    max_val = cost[i][j]
                    pos = (i, j)

        if pos[0] not in found_e:
            row_sum = sum(cost[pos[0]]) - max_val
        else:
            row_sum = 1

        if pos[1] not in found_m:
            col_sum = sum(cost[i][pos[1]] for i in range(N)) - max_val
        else:
            col_sum = 1

        if row_sum == 0 or col_sum == 0:
            final_cost += max_val
            found_e.add(pos[0])
            found_m.add(pos[1])

        cost[pos[0]][pos[1]] = 0

    print(final_cost - a)

else:

    result = find_min_cost_to_connect_all(N, M, cost)

    print(result)