file_names = [
    "python chapter 1 homework submission.csv",
    "python chapter 2 homework submission.csv",
    "python chapter 3-1 homework submission.csv",
    "python chapter 3-2 homework submission.csv",
    "python chapter 5 homework submission.csv",
    "python chapter 6 homework submission.csv",
    "python chapter 7 homework submission.csv",
    "python chapter 8 homework submission.csv",
]

new_file_name = []

for name in file_names:
    file_names = name.split(" ")
    # print(file_names)
    new_set = "py_ch" + file_names[2] + "_hw_submitted.csv"
    new_file_name.append(new_set)

print(new_file_name)
