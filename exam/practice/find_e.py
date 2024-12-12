from math import e

n = 1
real_e = e
error = 0.001

while True:
    val = (1 + (1 / n)) ** n
    if abs(val - real_e) < error:
        break
    n += 1

print(f"{val}")
