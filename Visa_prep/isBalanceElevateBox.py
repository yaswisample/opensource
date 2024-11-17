def c():
    N = int(input())
    A = list(map(int,input().split()))
    t= sum(A)
    lw = 0
    ba = []
    for i in range(N):
        rw = t - lw - A[i]
        b = abs(lw - rw)
        ba.append(b)
        lw  += A[i]
    print(" ".join(map(str,ba)))
c()
