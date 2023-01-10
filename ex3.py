try:
    a = int(input("a-> "))
    for i in range(a):
        for j in range(a):
            print('*' if i in [0, a-1] or j in [0, a-1] else ' ', end='')
        print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')