# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/the-enchanted-mirrors-reflection

def is_confusing_number(num):
    reflection_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    original = str(num)
    reflected = ""
    
    for digit in reversed(original):
        if digit not in reflection_map:
            return False
        reflected += reflection_map[digit]
    
    return reflected != original

def dfs(num_str, N):
    global confusing_count
    
    if num_str:
        num = int(num_str)
        
        if num <= N and is_confusing_number(num):
            confusing_count += 1
        
        if num > N:
            return
    
    for digit in ['0', '1', '6', '8', '9']:
        if not (num_str == "" and digit == '0'):
            dfs(num_str + digit, N)

def count_confusing_numbers(N):
    global confusing_count
    confusing_count = 0
    
    for digit in ['1', '6', '8', '9']:
        dfs(digit, N)
    
    return confusing_count

N = int(input().strip())
print(count_confusing_numbers(N))