def sum_of_odd_numbers(n):
    ### BEGIN SOLUTION

    if n > 0:
        list_num = range(1, n * 2, 2)
        sum_of_odd = sum(list(list_num))
        return sum_of_odd
    if n == 0:
        return 0
    ### END SOLUTION


# ลองทดสอบฟังก์ชัน
print(sum_of_odd_numbers(5))  # ผลลัพธ์์ที่คาดหวัง คือ 25
# For test-run
# ห้ามแก้ไขเซลล์นี้โดดเด็ดขาด (ไม่ตรวจ if แก้ไข)
# หลังจากเขียนโค้ดเสร็จ ให้กดรันเซลล์นี้ ถ้าแสดงผลลัพธ์ ```ผ่าน``` ถือว่าผ่าน (ทดสอบทั้งหมด 4 cases)


def run_tests():
    # ทดสอบกรณีที่ 1: n = 5
    result = sum_of_odd_numbers(5)
    expected = 25
    if result == expected:
        print("ทดสอบกรณีที่ 1 ผ่าน")
    else:
        print(f"ทดสอบกรณีที่ 1 ไม่ผ่าน: ผลลัพธ์ที่ได้ {result}, คาดหวัง {expected}")

    # ทดสอบกรณีที่ 2: n = 1 (กรณีขอบเขตที่น้อยที่สุด)
    result = sum_of_odd_numbers(1)
    expected = 1
    if result == expected:
        print("ทดสอบกรณีที่ 2 ผ่าน")
    else:
        print(f"ทดสอบกรณีที่ 2 ไม่ผ่าน: ผลลัพธ์ที่ได้ {result}, คาดหวัง {expected}")

    # ทดสอบกรณีที่ 3: n = 0 (กรณีขอบเขตที่ไม่ถูกต้อง, คาดหวังผลลัพธ์เป็น 0 เนื่องจากไม่มีเลขคี่)
    result = sum_of_odd_numbers(0)
    expected = 0
    if result == expected:
        print("ทดสอบกรณีที่ 3 ผ่าน")
    else:
        print(f"ทดสอบกรณีที่ 3 ไม่ผ่าน: ผลลัพธ์ที่ได้ {result}, คาดหวัง {expected}")

    # ทดสอบกรณีที่ 4: n = 10
    result = sum_of_odd_numbers(10)
    expected = 100
    if result == expected:
        print("ทดสอบกรณีที่ 4 ผ่าน")
    else:
        print(f"ทดสอบกรณีที่ 4 ไม่ผ่าน: ผลลัพธ์ที่ได้ {result}, คาดหวัง {expected}")

    # เพิ่มกรณีทดสอบต่อไปตามต้องการ


# ให้ทำการเรียกฟังก์ชัน run_tests() เพื่อทดสอบ
run_tests()
