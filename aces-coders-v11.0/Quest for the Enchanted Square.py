# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/quest-for-the-enchanted-square

import math

def distance_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def is_square(points):
    dists = []
    
    for i in range(4):
        for j in range(i + 1, 4):
            dists.append(distance_sq(points[i], points[j]))
    
    dists.sort()
    return dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] == 2 * dists[0]

points = []
for i in range(4):
    x, y = map(int, input().split())
    points.append((x, y))

if is_square(points):
    print("true")
else:
    print("false")