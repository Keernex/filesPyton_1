try:
    with open("hello.txt", 'r+') as file:
        cont = file.readlines()
        q=int(input())
        cont[q-1] = "" + "\n"
        print(cont)
        file.seek(0)
        file.writelines(cont)
except Exception as e:
    print("Error: " + e)
