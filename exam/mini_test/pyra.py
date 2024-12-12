n = int(input("Number : "))

for j in range(n):
    for i in range(n - j - 1):
        print("5", end="")
    for i in range(j * 2 + 1):
        print("*", end="")
    for i in range(n - j - 1):
        print("5", end="")
    print()
