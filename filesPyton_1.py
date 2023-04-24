try:
    with open('hello.txt', 'r') as file:
        contents = file.read().split()
        print(len(contents))
except Exception as e:
    print("Error: " + e)
