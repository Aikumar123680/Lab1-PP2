import re

camel=str(input())
x=re.sub(r"(\w)([A-Z])", r"\1_\2", camel).lower()
print(x) 