import re

txt=str(input())
x=re.findall(r"^[a-z]+_[a-z]+$", txt)
if(x):
    print(f"Matches:{x}")
else:
    print("No matches")