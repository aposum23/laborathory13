def print_these(a, b, c):
    print(a, 'is stored in a')
    print(b, 'is stored in b')
    print(c, 'is stored in c')

print_these(1, 2, 3)



def print_these(a, b, c=None):
    print(a, 'is stored in a')
    print(b, 'is stored in b')
    print(c, 'is stored in c')

print_these(1, 2)


def print_these(a=None, b=None, c=None):
    print(a, 'is stored in a')
    print(b, 'is stored in b')
    print(c, 'is stored in c')

print_these(c=3, a=1)
