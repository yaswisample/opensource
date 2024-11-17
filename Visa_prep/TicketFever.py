T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    students_without_tickets = max(0, N - M)
    print(students_without_tickets)
