try:
    a = int(input("a-> "))
    b = int(input("b-> "))
    for i in range(a):
        for j in range(b):
            print('*', end="")
        print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
