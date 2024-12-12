str1 = "PYNative39@kmitl8496.com"

list_number = []

for chr in str1:
    if ord(chr) in range(ord("0"), ord("9") + 1):
        list_number.append(int(chr))

sum_number = sum(list_number)
avg = sum_number / len(list_number)

print(f"sum = {sum_number} and avg = {avg}")
