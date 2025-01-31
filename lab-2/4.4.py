fruits = ("apple", "banana", "cherry")



fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)




fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)




thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)



thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])




thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1