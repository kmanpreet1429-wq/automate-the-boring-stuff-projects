
num_of_inputs = int(input())
arr = list(map(int, input().split()))

highest = max(arr)
while highest in arr:
    arr.remove(highest)
runner_up = max(arr)
print(runner_up)


