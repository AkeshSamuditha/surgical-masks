# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/the-holiday-shuffle
def reverse_bits(n, P):
    bin_n = bin(n)[2:].zfill(P)
    reversed_bin_n = bin_n[::-1]
    return int(reversed_bin_n, 2)

P = int(input())
n = int(input())

city_number = reverse_bits(n, P)
print(city_number)