import re

txt=str(input())
x=re.sub(r"([a-z])([_])([a-z])",r"\1\3",txt)
print(x)