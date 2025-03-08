source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")

try:
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())
    print(f"Contents copied from {source} to {destination}")
except FileNotFoundError:
    print("Source file not found.")