file_path = input("Enter the file path: ")

try:
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    print(f"Total number of lines: {line_count}")
except FileNotFoundError:
    print("File not found.")