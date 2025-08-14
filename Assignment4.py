#Task1 Read a file and handle errors

try:
    with open ("sample.txt", "r") as file:
        f=file.read()
        print(f)
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")

#Task2 Write and append data to the file

with open ("output.txt", "w") as file:
    file.write("Hello, Python!\n")
    print("Data successfully written to 'output.txt'")
with open ("output.txt", "a") as file:
    file.write("Learning file handling in python")
    print("Data successfully appended to file")
with open ("output.txt", "r") as file:
    print("Final contents of 'output.txt':")
    f1=file.read()
    print(f1)



