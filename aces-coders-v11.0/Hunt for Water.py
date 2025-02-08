# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/hunt-for-water
def calculate_water_capacity(n, d, t, heights):
    if n <= 2:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    total_water = 0
    for i in range(1, n - 1):
        water_height = min(left_max[i], right_max[i]) - heights[i]
        if water_height > 0:
            total_water += water_height

    return total_water * d * t

n, d, t = map(int, input().split())
heights = list(map(int, input().split()))
result = calculate_water_capacity(n, d, t, heights)
print(result)