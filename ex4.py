try:
    a = int(input("a-> "))
    b = int(input("b-> "))
    for i in range(a):
        for j in range(b):
            print('*' if i in [0, a-1] or j in [0, b-1] else ' ', end='')
        print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
