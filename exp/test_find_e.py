from math import e, fabs as abs, pow

e_true = e
n = 1
error = 1e-5


def find(n):
    while True:
        lim_e = pow(1 + (1 / n), n)
        if abs(lim_e - e_true) < error:
            break
        n += 1
    return lim_e


result = find(n)
print(f"result of e = {result:.5f}")
