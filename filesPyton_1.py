try:
    with open("hello.txt", "r", encoding="utf8") as _file:
        q=input()
        for line in _file:
            if q in line:
                print(line, end="")
except Exception as e:
    print("Error: " + e)
