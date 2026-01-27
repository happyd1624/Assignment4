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
