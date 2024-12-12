# str1 = "PYNative39@kmitl8496.com"
# ### BEGIN SOLUTION
# sum = 0
# count_ch = 0
# for ch in str1:
#     if ord(ch) >= ord("0") and ord(ch) <= ord("9"):
#         sum += int(ch)

str1 = "PYNative39@kmitl8496.com"
list_number = []


def avg_num(sentence):
    for ch in sentence:
        if ord(ch) in range(ord("0"), ord("9") + 1):
            list_number.append(int(ch))
    avg = sum(list_number) / len(list_number)
    return avg


print(avg_num(str1))
