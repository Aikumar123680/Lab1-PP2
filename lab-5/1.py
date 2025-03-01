import re 

txt=str(input())
x= re.findall(r"ab*", txt)
if(x):
    print(f"Mathces:{x}")