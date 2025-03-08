import string

for letter in string.ascii_uppercase:  # A-Z
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is {filename}\n")
print("26 files (A.txt to Z.txt) created.")