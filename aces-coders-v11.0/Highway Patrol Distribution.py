# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/highway-patrol-distribution/problem
# Achived 42.31 points out of 50 which was the highest score in the contest. Test case 10 and 14 throwed runtime error.

def read_input():
    N = int(input())
    traffic = []
    for _ in range(N):
        t = int(input())
        traffic.append(t)
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1  # Convert to 0-based index
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    return N, traffic, tree

def dfs(node, parent, traffic, tree, subtree_sum, entry_exit, time, parent_list):
    entry_time = time[0]
    time[0] += 1
    total = traffic[node]
    parent_list[node] = parent
    for child in tree[node]:
        if child != parent:
            total += dfs(child, node, traffic, tree, subtree_sum, entry_exit, time, parent_list)
    subtree_sum[node] = total
    exit_time = time[0]
    time[0] += 1
    entry_exit[node] = (entry_time, exit_time)
    return total

def is_ancestor(u, v, entry_exit):
    # Returns True if u is an ancestor of v
    entry_u, exit_u = entry_exit[u]
    entry_v, exit_v = entry_exit[v]
    return entry_u <= entry_v and exit_v <= exit_u

def solve(N, traffic, tree):
    total_sum = sum(traffic)
    subtree_sum = [0] * N
    entry_exit = [(-1, -1)] * N
    time = [0]
    parent_list = [-1] * N
    dfs(0, -1, traffic, tree, subtree_sum, entry_exit, time, parent_list)
    edges = []
    for node in range(N):
        if parent_list[node] != -1:
            edges.append((node, parent_list[node]))
    min_max_traffic = float('inf')
    edge_info = []
    for child, parent_node in edges:
        edge_info.append({
            'child': child,
            'sum': subtree_sum[child],
            'entry': entry_exit[child][0],
            'exit': entry_exit[child][1]
        })
    num_edges = len(edge_info)
    for i in range(num_edges):
        for j in range(i + 1, num_edges):
            c1 = edge_info[i]['child']
            c2 = edge_info[j]['child']
            s1 = subtree_sum[c1]
            s2 = subtree_sum[c2]
            if is_ancestor(c1, c2, entry_exit):
                sumA = s2
                sumB = s1 - s2
                sumC = total_sum - s1
            elif is_ancestor(c2, c1, entry_exit):
                sumA = s1
                sumB = s2 - s1
                sumC = total_sum - s2
            else:
                sumA = s1
                sumB = s2
                sumC = total_sum - s1 - s2
            current_max = max(sumA, sumB, sumC)
            if current_max < min_max_traffic:
                min_max_traffic = current_max
    if min_max_traffic == float('inf'):
        for info in edge_info:
            sumA = info['sum']
            sumB = total_sum - sumA
            current_max = max(sumA, sumB)
            if current_max < min_max_traffic:
                min_max_traffic = current_max
    if min_max_traffic == float('inf'):
        min_max_traffic = total_sum
    return min_max_traffic

N, traffic, tree = read_input()
result = solve(N, traffic, tree)
print(result)