# Calculate f(x)= x**2+6x+5 = 0 using Newton's Method


x = 8
x_new = 0
error = 1e-16
start_count = 0
end_count = 1000

while True:
    fx = (x**2) + (6 * x) + 5
    dfx = (2 * x) + 6
    x_new = x - (fx / dfx)
    if abs(x_new - x) < error or start_count > end_count:
        break
    x = x_new
    start_count += 1

print(f"result of equation = {x}")
