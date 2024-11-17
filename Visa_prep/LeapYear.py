X=int(input())
if 1500<=X<=3000:
    if(X%4==0 and X%100!=0) or (X%4==0 and X%400==0):
        print("YES")
    else:
        print("NO")
