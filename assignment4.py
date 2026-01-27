#task1

def read_sample_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file
                print(line.strip())
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_sample_file("sample.txt")


#task2


user_data = input("Enter data to write: ")
with open("output.txt", "w") as file:
    file.write(user_data + "\n")

additional_data = input("Enter data to append: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

print("\nFinal Content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
