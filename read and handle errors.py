filename = input("Enter the Filename: ")

try:
    with open(filename,'r') as file1:
        line_number = 1
        print("Reading file contents:")
        for line in file1:
            print("line ",line_number,":",line)
            line_number = line_number + 1
except FileNotFoundError:
    print("Error: The file ",filename, "was not found.")