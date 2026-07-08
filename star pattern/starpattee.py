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

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()#hollow square

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()#hollow triangle


n = 5

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()#hollow pyramid


n = 5

for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)#butterfly


n = 5

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)

for i in range(2, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)#sandglass


n = 5

for i in range(n):
    print(" " * i + "*" * (2 * (n - i) - 1))

for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))#hourglass


n = 5

for i in range(n):
    num = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()#pascal triangle


n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()#floyd's triangle


n = 5

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
