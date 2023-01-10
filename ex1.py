try:
    for i in range(1, 4):
        for j in range(1, 4):
            print('*', end="")
        print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')