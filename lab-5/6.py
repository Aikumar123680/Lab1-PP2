import re

txt=str(input())
x=re.sub(r"[\s,.]",":",txt)
if(x):
    print(f"{x}")
else:
    print("No matches")