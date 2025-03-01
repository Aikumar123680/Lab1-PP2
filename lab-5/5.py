import re

txt=str(input())
x=re.findall(r"^a[a-z]*b$",txt)
if(x):
    print(f"Matches:{x}")
else:
    print("No matches")