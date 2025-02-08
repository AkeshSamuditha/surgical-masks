# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/design-the-largest-aquarium

def max_water_volume(heights):
    left, right = 0, len(heights) - 1
    max_volume = 0
    
    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        volume = height * width
        max_volume = max(max_volume, volume)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_volume

n = int(input())
heights = list(map(int, input().split()))

print(max_water_volume(heights))