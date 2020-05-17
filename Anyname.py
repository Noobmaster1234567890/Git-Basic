def lalala():
    try :
        a=int(input('Type a number: '))
        b=int(input('Type another number: '))
        z=str(input('Addition, Subtraction, Multiplication, or Division: '))
        if z == 'Addition':
            print(a+b)
        if z == 'Subtraction':
            print(a-b)
        if z == 'Multiplication':
            print(a*b)
        if z == 'Division':
            print(a/b)
    except:
        print('You Suck Bye Bye')
lalala()
