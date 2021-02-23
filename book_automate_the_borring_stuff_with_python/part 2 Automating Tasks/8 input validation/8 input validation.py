while True
    age = input('enter age: ')
    try:
        age = int(age)
    except:
        print('enter digits')
    if age < 1:
        print('pls enter positive number')
    else:
        break