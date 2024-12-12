from math import sqrt as root

input_num = input("Enter number : ")
num = input_num.split()


def cal_rms2(*num, places=2):
    sum = 0
    N = len(num)
    if N == 0:
        return None
    if N > 0:
        for n in num:
            sum += int(n) ** 2
        rms = root(sum / N)
        rms_round = round(rms, places)
        return rms_round


print(cal_rms2(*num))
