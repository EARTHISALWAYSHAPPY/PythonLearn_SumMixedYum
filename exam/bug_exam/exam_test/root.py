def seven_root(n):
    x = n
    error = 0.0001
    while True:
        x_new = ((6 * x) + (n / x**6)) / 7
        if abs(x_new - x) < error:
            break
        x = x_new
    return x


print(seven_root(3))
