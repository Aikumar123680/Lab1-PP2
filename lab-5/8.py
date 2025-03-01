import re

txt=str(input())
x=re.split(r"(?=[A-Z])",txt)
print(x)