input_str=input()
A,B,C,X=map(int,input_str.split())
if(A+B>=X)or(A+C>=X)or(B+C>=X):
    print("YES")
else:
    print("NO")
