# from math import sqrt

# num = [3, 5, 7, 9, 11]


# def cal_rms(*num, places=2):
#     sum = 0
#     N = len(num)
#     if N == 0:
#         return None
#     if N > 0:
#         for n in num:
#             sum += int(n) ** 2
#         rms = sqrt(sum / N)
#         round_rms = round(rms, places)
#         return round_rms


# print(cal_rms(*num))

n = 5
for j in range(n):
    for i in range(n - j):
        print(" ", end="")
    for i in range(j + 1):
        print("*", end=" ")
    print()
