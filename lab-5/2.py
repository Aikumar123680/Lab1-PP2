import re

txt=str(input())
x=re.findall(r"ab{2,3}",txt)
if(x):
    print(f"Matches:{x}")
else:
    print("No matches")