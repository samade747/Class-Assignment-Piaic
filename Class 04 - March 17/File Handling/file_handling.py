# file_handling.py

# -----------------------------------
# 1. Writing to a File
# -----------------------------------

print("🔹 Writing to a file (write mode)")

file = open("example.txt", "w")
file.write("Hello, this is a new file.\n")
file.write("Welcome to file handling in Python.\n")
file.close()

print("Data written to example.txt\n")

# -----------------------------------
# 2. Reading from a File
# -----------------------------------

print("🔹 Reading the file content")

file = open("example.txt", "r")
content = file.read()
file.close()

print("File content:\n", content)

# -----------------------------------
# 3. Appending to a File
# -----------------------------------

print("🔹 Appending to the file")

file = open("example.txt", "a")
file.write("This line is added using append mode.\n")
file.close()

print("Appended new line to example.txt\n")

# -----------------------------------
# 4. Reading Line by Line
# -----------------------------------

print("🔹 Reading line by line")

file = open("example.txt", "r")
for line in file:
    print(line.strip())
file.close()

# -----------------------------------
# 5. Using 'with' Statement (Best Practice)
# -----------------------------------

print("\n🔹 Using 'with' statement")

with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Reading using with statement:")
    for line in lines:
        print(line.strip())
