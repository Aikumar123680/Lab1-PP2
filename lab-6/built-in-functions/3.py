def is_palindrome(s):
    return s == s[::-1]

x=str(input())
if is_palindrome(x):
    print("Yes it is")
else:
    print("No")