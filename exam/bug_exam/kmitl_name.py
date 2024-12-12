kmitl_names = [
    "somchai sombat",
    "supaporn thongdee",
    "narongchai wongthan",
    "saranya chaisongkram",
    "chatchai phrompraphan",
    "wanida saengthong",
    "natthaporn promma",
    "nattapol maneesong",
    "kittiphong thongkham",
    "chanakan klaewklong",
]
temp_list = []
kmitl_emails = []
for name in kmitl_names:
    temp_list = name.split(" ")
    new_name = temp_list[0] + "." + temp_list[1][0:2] + "@kmitl.ac.th"
    kmitl_emails.append(new_name)

print(kmitl_emails)
