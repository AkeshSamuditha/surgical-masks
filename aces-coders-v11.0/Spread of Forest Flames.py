# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/spread-of-forest-flames

from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

queue = deque()
time = [[-1] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if grid[i][j] == 2:
            queue.append((i, j))
            time[i][j] = 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and time[nx][ny] == -1:
            time[nx][ny] = time[x][y] + 1
            queue.append((nx, ny))

max_time = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1 and time[i][j] == -1:
            print(-1)
            exit()
        max_time = max(max_time, time[i][j])

print(max_time)