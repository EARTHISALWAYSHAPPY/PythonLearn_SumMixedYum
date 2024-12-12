def cube_root(n):
    # กำหนดค่าเริ่มต้น
    x = n / 2  # เริ่มต้นที่ครึ่งของค่า n

    # ใช้วิธีนิวตันในการคำนวณ
    while abs(x**3 - n) > 0.0001:
        x = (2 * x + n / x**2) / 3

    return x


# ทดสอบ
result = cube_root(9)
print(f"The cube root of 27 is approximately: {result}")
