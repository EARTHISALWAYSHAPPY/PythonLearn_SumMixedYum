n = int(input("Enter your number find sqr root : "))


def sqr_root(n):
    x = n
    error = 1e-5
    while True:
        fx = x**2 - n
        dfx = 2 * x
        x_new = x - (fx / dfx)
        if abs(x_new - x) < error:
            break
        x = x_new
    return x


result = sqr_root(n)
print(f"result of number is {result:.3f}")
