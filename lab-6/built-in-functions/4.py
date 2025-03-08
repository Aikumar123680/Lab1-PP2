from functools import reduce
import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

x=int(input())
y=int(input())
l=delayed_sqrt(x, y)
print(f"Square root of {x} after {y} miliseconds is {l}")

    