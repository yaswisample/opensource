X,Y,Z=map(int,input().split())
time_taken=X*Y
Z=Z*24*60
if time_taken <= Z:
    print("YES")
else:
    print("NO")
