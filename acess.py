print("What is your name?")

name = input()
password = "123456"

if name == "Georgi":
    print("Hello, G")
    if password == "123456":
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Wrong user")
