import re

txt=str(input())
x=re.findall(r"^[A-Z][a-z]*$",txt)
if(x):
    print(f"Matches:{x}")
else:
    print("No Matches")