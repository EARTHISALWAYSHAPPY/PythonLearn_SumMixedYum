n = int(input("Enter your number find cube root : "))


def cube_root(n):
    x = n
    error = 1e-5
    while True:
        x_new = ((2 * x) + (n / x**2)) / 3
        if abs(x_new - x) < error:
            break
        x = x_new
    return x


print(f"{cube_root(n):.3f}")
