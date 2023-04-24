try:
    with open("hello.txt", 'r') as file:
        cont = file.readlines()
        q=set()
        for i in cont:
            if i in cont:
                print("Повторення є")
                break
except Exception as e:
    print("Error: " + e)
