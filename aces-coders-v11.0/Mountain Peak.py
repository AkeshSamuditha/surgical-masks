# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/mountain-peak
def next_greater_peak(heights):
    n = len(heights)
    result = [-1] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= heights[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(heights[i])
    return result


N = int(input())
height_list = list(map(int, input().split()))
result = next_greater_peak(height_list)
print(" ".join(map(str, result)))