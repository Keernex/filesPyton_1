try:
    with open("hello.txt", 'r+') as file:
        cont = file.readlines()
        sor = sorted(cont)
        file.seek(0)
        file.writelines(sor)
        file.truncate()
except Exception as e:
    print("Error: " + e)
