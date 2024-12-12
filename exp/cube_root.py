from math import fabs as abs


def cube_root(n):
    ### BEGIN SOLUTION
    if n == 0:
        return 0
    x = n / 3
    error = 0.0001
    while True:
        x_new = x - ((x**3 - n) / (3 * (x**2)))
        if abs(x_new - x) < error:
            break
        x = x_new
    return x * (-1 if n < 0 else 1)


n = int(input("Enter a number to find cube root: "))

### END SOLUTION

# ลองทดสอบฟังก์ชัน
print(cube_root(n))  # ผลลัพธ์ที่คาดหวังใกล้เคียง 3
