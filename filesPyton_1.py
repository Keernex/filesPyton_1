try:
    with open("hello.txt", 'r+') as file:
        cont = file.readlines()
        q=int(input())
        w=input()
        cont[q] = w + '\n'
        file.seek(0)
        file.writecont(cont)
        file.truncate()
except Exception as e:
    print("Error: " + e)
