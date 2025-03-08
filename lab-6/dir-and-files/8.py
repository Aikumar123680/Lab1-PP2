import os

file_path = input("Enter the file path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):  # Check if writable (to allow deletion)
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")
    else:
        print("No permission to delete the file.")
else:
    print("File does not exist.")