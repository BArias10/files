#Files Assignment Week 8

def main():
    directory = input("Enter Directory You Want To Save: ")
    file_name = input("Enter Filename: ")
    name = input("Enter Your Name: ")
    phone_number = input("Enter Your Phone Number: ")
    address = input("Enter Your Address: ")
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory, file_name), 'w')
        writeFile.write(name + ',' + address + ',' + phone_number + '\n')
        writeFile.close()

        print("File Contents:")
        readFile = open(os.path.join(directory, file_name), 'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Directory Does Not Exist!")
main()
