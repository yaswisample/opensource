def is_sorted():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return "false"
    return "true"
print(is_sorted())
