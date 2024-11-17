N=int(input())
if 1<=N<=12:
    if 3<=N<=5:
        print("Spring")
    elif 6<=N<=8:
        print("Summer")
    elif 9<=N<=11:
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
