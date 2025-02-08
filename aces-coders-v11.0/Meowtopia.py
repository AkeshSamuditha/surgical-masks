def dfs(cat, territory_map, visited):
    visited[cat] = True
    for neighbor in range(len(territory_map)):
        if territory_map[cat][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, territory_map, visited)

def count_catdoms(n, territory_map):
    visited = [False] * n
    catdom_count = 0

    for cat in range(n):
        if not visited[cat]:
            dfs(cat, territory_map, visited)
            catdom_count += 1

    return catdom_count

n = int(input())
territory_map = []

for _ in range(n):
    territory_map.append(list(map(int, input().split())))

result = count_catdoms(n, territory_map)
print(result)