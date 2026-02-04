# Task 1
filename_read = "sample.txt"

try:
    with open(filename_read, "r") as file:
        print("Reading file content:")
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename_read}' was not found.")

print("\n" + "-"*10 + "\n")


# Task 2
filename_write = "output.txt"

first_input = input("Enter text to write to the file: ")
with open(filename_write, "w") as file:
    file.write(first_input + "\n")
print(f"Data successfully written to {filename_write}.\n")

second_input = input("Enter additional text to append: ")
with open(filename_write, "a") as file:
    file.write(second_input + "\n")
print("Data successfully appended.\n")

print(f"Final content of {filename_write}:")
with open(filename_write, "r") as file:
    print(file.read())
