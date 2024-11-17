def reduce_string(s):
    if not s: 
        return ""
    reduced_string = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            reduced_string += s[i - 1] + str(count)
            count = 1
    reduced_string += s[-1] + str(count)
    return reduced_string
s = input().strip()
print(reduce_string(s))
