try:
    with open("hello.txt", "r") as _file:
        q=int(input())
        cont = _file.readlines()
        for i in range(q*-1,-1+1):
            print(cont[i],end="")
except Exception as e:
    print("Error: " + e)
