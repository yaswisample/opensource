def rotate_by_one(arr):
    return arr[1:] + arr[:1]
N = int(input())
arr = list(map(int, input().split()))
result = rotate_by_one(arr)
print(*result)
