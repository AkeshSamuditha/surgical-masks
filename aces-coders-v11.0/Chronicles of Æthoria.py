# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/chronicles-of-aethoria
# Hard
from collections import deque

def has_cycle_dfs(maze, node, visited, parent, start):
    visited[node] = True
    for neighbor in range(len(maze)):
        if maze[node][neighbor] == 1:
            if not visited[neighbor]:
                if has_cycle_dfs(maze, neighbor, visited, node, start):
                    return True
            elif neighbor == start and parent != neighbor:
                return True
    return False

def has_path_dfs(maze, node, visited, target):
    visited[node] = True
    if node == target:
        return True
    for neighbor in range(len(maze)):
        if maze[node][neighbor] == 1 and not visited[neighbor]:
            if has_path_dfs(maze, neighbor, visited, target):
                return True
    return False

def bfs_shortest_path(maze, start, N):
    dist = [-1] * N
    dist[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in range(N):
            if maze[node][neighbor] == 1 and dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist

def find_optimal_cornered_portal(maze, S, C, dist_from_C, N):
    visited_S = [False] * N
    visited_S[S] = True
    queue = deque([(S, 0)])
    optimal_portal = S 
    max_time_to_catch = dist_from_C[S]
    
    while queue:
        node, steps = queue.popleft()

        if dist_from_C[node] > max_time_to_catch:
            max_time_to_catch = dist_from_C[node]
            optimal_portal = node

        for neighbor in range(N):
            if maze[node][neighbor] == 1 and not visited_S[neighbor]:
                if dist_from_C[neighbor] > steps + 1: 
                    visited_S[neighbor] = True
                    queue.append((neighbor, steps + 1))

    return optimal_portal, max_time_to_catch

T = int(input())

for _ in range(T):
    N, M, S, C = map(int, input().split())
    maze = [[0] * N for _ in range(N)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        maze[a-1][b-1] = 1
        maze[b-1][a-1] = 1
    
    portals_with_cycles = set()
    visited = [False] * N

    for i in range(N):
        if not visited[i]:
            visited_temp = [False] * N
            if has_cycle_dfs(maze, i, visited_temp, -1, i):
                portals_with_cycles.add(i)

    dist_from_S = bfs_shortest_path(maze, S - 1, N)
    dist_from_C = bfs_shortest_path(maze, C - 1, N)
    
    min_moves_S = float('inf')
    target_cycle_portal = -1 

    for portal in portals_with_cycles:
        if dist_from_S[portal] != -1:
            if dist_from_S[portal] < min_moves_S:
                min_moves_S = dist_from_S[portal]
                target_cycle_portal = portal
    
    steps_to_S = dist_from_C[S - 1]
    
    if not has_path_dfs(maze, S -1, visited, C - 1):
        print("SAFE")
        continue
    if target_cycle_portal != -1:
        moves_for_C = dist_from_C[target_cycle_portal]
        if min_moves_S < moves_for_C:
            print("SAFE")
        else:
            corner, moves_for_C = find_optimal_cornered_portal(maze, S - 1, C - 1, dist_from_C, N)
            print(moves_for_C*2)
    else:
        corner, moves_for_C = find_optimal_cornered_portal(maze, S - 1, C - 1, dist_from_C, N)
        print(moves_for_C*2)