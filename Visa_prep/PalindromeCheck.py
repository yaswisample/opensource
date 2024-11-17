    
def is_palindrome(s):
    return s == s[::-1]
S = input().strip()
if is_palindrome(S):
    print("TRUE")
else:
    print("FALSE")
