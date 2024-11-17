def max_consecutive_absent_days(attendance):
    max_count = 0
    current_count = 0
    for day in attendance:
        if day == 0:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count
N = int(input())
attendance = list(map(int, input().split()))
print(max_consecutive_absent_days(attendance))
