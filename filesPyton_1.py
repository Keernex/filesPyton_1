try:
    with open("hello.txt", "r") as file:
        print(file.read())
except Exception as e:
    print("Error: " + e)
