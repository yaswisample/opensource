T = int(input())
for _ in range(T):
    X, N = map(int,input().split())
    score = N * (X // 10)
    print(score)
