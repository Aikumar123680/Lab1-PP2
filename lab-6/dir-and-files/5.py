data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
file_path = "fruits.txt"

with open(file_path, 'w') as file:
    for item in data:
        file.write(item + "\n")

print(f"List written to {file_path}")