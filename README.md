# Assignment4

# Task 1
Created a function to read a file and handle errors .. used a try-except block to manage the file operations .. 
in the try block opened the file named sample.txt using with open in read mode ..
used a for loop with enumerate to iterate through the file and print each line with its line number using strip() to remove extra spaces .. 
in the except block used FileNotFoundError to catch if the file is missing .. at last printing a custom error message if the file does not exist.

# Task 2
Took user input and opened a file named output.txt in write mode to store the initial data ..
used the write function to save the input which clears the file first ..
then opened the same file in append mode using 'a' to add more information to the end of the file .. 
used another write operation to add the additional data without losing the first part .. at last opened the file in read mode to read the entire content and printed the final result to the console.
