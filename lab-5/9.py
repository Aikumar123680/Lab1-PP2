import re

txt="TheWorldWide"
x=re.sub(r"(\w)([A-Z])",r"\1 \2",txt)
print(x)