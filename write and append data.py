file1 = open('output.txt', 'w')
first = input("Enter text to write to the file: ")
write_file = file1.write(first)
file1.close()

print("Data successfully written to output.txt.")

file1 = open('output.txt','a')
second = input("Enter additional text to append: ")
append_file = file1.write('\n' + second)
file1.close()

print("Data successfully appended.")

file1 = open('output.txt','r')
read_file = file1.read()
print("Final contents of output.txt: ")
print(read_file)
file1.close()