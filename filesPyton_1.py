try:
    with open("hello.txt", "r") as _file:
        cont = _file.read()
        for i in cont:
            if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
                print(i, end=" ")
except Exception as e:
    print("Error: " + e)
