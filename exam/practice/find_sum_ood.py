num = int(input("Many of number : "))
sum_num = 0


def sum_ood(x):
    if x == 0:
        return 0
    elif x > 0:
        sum_num = sum(range(1, x * 2, 2))
        return sum_num
    elif x < 0:
        return None


print(sum_ood(num))
