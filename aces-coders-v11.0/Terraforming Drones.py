# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/terraforming-drones

def alienTerraforming(n, grid):
    r, c = len(grid), len(grid[0])
    def get_new_grid():
        return [['D' for _ in range(c)] for _ in range(r)]
    
    def burst_drones(current_grid):
        new_grid = get_new_grid()
        for i in range(r):
            for j in range(c):
                if current_grid[i][j] == 'D':
                    new_grid[i][j] = '.'
                    if i > 0: new_grid[i - 1][j] = '.'
                    if i < r - 1: new_grid[i + 1][j] = '.'
                    if j > 0: new_grid[i][j - 1] = '.'
                    if j < c - 1: new_grid[i][j + 1] = '.'
        return new_grid

    if n == 1:
        return grid
    elif n % 2 == 0:
        return get_new_grid()
    else:
        first_burst = burst_drones(grid)
        second_burst = burst_drones(first_burst)
        return first_burst if (n % 4 == 3) else second_burst

r, c, n = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
result = alienTerraforming(n, grid)
for row in result:
    print("".join(row))
