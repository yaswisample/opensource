def reverse_array():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.reverse()
    print(" ".join(map(str,arr)))
reverse_array()
