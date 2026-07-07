n = 5

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()#square pattern 

    n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()#left triangle

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()#inverted triangle

n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end="")
    print()#right triangle

n = 5

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end="")
    print()#inverted right triangle

n = 5

for i in range(n):
    print(" " * (n - i - 1), end="")
    print("* " * (i + 1))#pyramid

n = 5

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)#inverted pyramid

n = 5

for i in range(n):
    print(" " * (n - i - 1), end="")
    print("* " * (i + 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)#diamond

