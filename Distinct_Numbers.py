import sys

n = int(sys.stdin.readline())  # Read 'n'
nums = input().split()  # Read all numbers as strings

distinct_numbers = set(nums)  # Use set directly on strings (avoids int conversion overhead)
print(len(distinct_numbers))  # Output distinct count

