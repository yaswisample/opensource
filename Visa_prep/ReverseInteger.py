def reverse_integer(n):
    is_negative = n < 0
    n = abs(n)
    reversed_n = int(str(n)[::-1])
    if is_negative:
        reversed_n = -reversed_n
    if reversed_n < -2**31 or reversed_n > 2**31 - 1:
        return 0
    return reversed_n
n = int(input().strip())
print(reverse_integer(n))
