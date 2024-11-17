def unique_elements(arr):
    unique_set = set()
    unique_list = []
    for num in arr:
        if num not in unique_set:
            unique_set.add(num)
            unique_list.append(num)
    return unique_list
N = int(input())
arr = list(map(int, input().split()))
result = unique_elements(arr)
print(*result)
