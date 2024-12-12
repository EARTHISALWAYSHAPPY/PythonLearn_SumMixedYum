n_list = [
    1,
    1e2,
    1e3,
    1e4,
    1e5,
    1e6,
    1e7,
    1e8,
    1e9,
    1e10,
    1e11,
    1e12,
    1e13,
    1e14,
    1e15,
    1e16,
]

for n in n_list:
    result = (1 + 1 / n) ** n
    print(f"(1+1/{n:.0e})^{n:.0e} = {result:.10f}")
# i = 0
# while i < len(n_list):
#     n = float(n_list[i])
#     result = (1 + 1 / n) ** n
#     print(f"(1+1/{n:.0e})^{n:.0e} = {result:.10f}")
#     i += 1
