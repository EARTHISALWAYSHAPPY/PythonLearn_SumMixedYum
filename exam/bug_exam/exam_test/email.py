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
eamils_names = []
for name in kmitl_names:
    temp_name = name.split(" ")
    email = temp_name[0] + "." + temp_name[1][:2] + "@kmitl.ac.th"
    eamils_names.append(email)

print(eamils_names)
