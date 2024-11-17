T = int(input().strip())
for _ in range(T):
    X, N = map(int,input().strip().split())
    points_per_test_case = X // 10
    score = points_per_test_case * N
    print(score)
