# n = int(input("Enter your number : "))


# def pyramid(n):
#     print(f"Level of pyramid : {n}")
#     for x in range(n):
#         for y in range(n - x - 1):
#             print(" ", end="")
#         for y in range(2 * x + 1):
#             print("*", end="")
#         print()


# pyramid(n)

############################################
n = int(input("Enter your number : "))


def pyramid(n):
    print(f"Level of pyramid : {n}")
    for x in range(n):
        for y in range(n - x):
            print(" ", end="")
        for y in range(x + 1):
            print("*", end=" ")
        print()


pyramid(n)
