def func(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

print("Upper and Lower case count:", func("Hello World!"))