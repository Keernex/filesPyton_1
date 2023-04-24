try:
    q=input()
    with open('hello.txt', 'r') as file:
        content = file.read()
        if q in content:
            print('Рядок знайдено')
        else:
            print('Рядок не знайдено')
except Exception as e:
    print("Error: " + e)
