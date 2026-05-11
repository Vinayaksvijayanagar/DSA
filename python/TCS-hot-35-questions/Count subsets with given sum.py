# Given T test cases. Each has an array of N integers and a target sum. Count the number of subsets
# of the array whose elements sum to the target. Print answer modulo 10^9+7.
# Sample input
# 2
# 6
# 2 3 5 6 8 10
# 10
# 5
# 1 2 3 4 5
# 10
# Sample output
# 3
# 3
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())

    def count_subsets(i, current_sum):
        # if sum reached target
        if current_sum == target:
            return 1
        
        # if out of bounds or sum exceeded
        if i == n or current_sum > target:
            return 0
        
        # take + not take
        take = count_subsets(i + 1, current_sum + arr[i])
        not_take = count_subsets(i + 1, current_sum)
        
        return take + not_take

    print(count_subsets(0, 0))