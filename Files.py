print("Welcome. People come here to create a "
    "file that will contain their information.\n")

directory = input("Please provide the directory for where"
    " you would like to store the file or where the file is stored: ")

file_name = input("Please provide the name of the file: ")

f_directory = directory + '/' + file_name

print(f_directory)
try:
    with open(f_directory) as f:
        contents = f.read()

except FileNotFoundError:
    with open(f_directory, 'w') as f:
        name = input("Please enter your name: ") + ", "
        address = input("Please enter your Address: ") + ", "
        number = input("Please enter your phone number: ")
        f.write(name)
        f.write(address)
        f.write(number)
    with open(f_directory) as f:
        contents = f.read()
        print(contents)

else:
    print(contents)

print("Thank you for using this useless tool.")