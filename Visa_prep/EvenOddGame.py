N = input()
sum_digits = sum(int(digit) for digit in N)
if sum_digits % 2 == 0:
    print("Vignesh")
else:
    print("Charan")
