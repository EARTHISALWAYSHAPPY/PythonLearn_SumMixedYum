def seventh_root(n):
    x = n
    error = 1e-5
    while True:
        x_new = ((6 * x) + (n / x**6)) / 7
        if abs(x_new - x) < error:
            break
        x = x_new
    return x


print(seventh_root(2097152))
