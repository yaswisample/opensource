Vignesh, Charan = input().split()
if Vignesh == Charan:
    print("NULL")
elif (Vignesh == "R" and Charan == "S") or (Vignesh == "P" and Charan == "R") or(Vignesh == "S" and Charan == "P"):
    print("Vignesh")
else:
    print("Charan")
