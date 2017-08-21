inp = input()
m, d = [int(x) for x in inp.split()]

total_d = 31

if m == 2:
    total_d = 28
elif m == 4 or m == 6 or m ==9  or m == 11:
    total_d = 30

total_d -= (8 - d)
total_cols = 1 + int(total_d/7)
if total_d % 7 != 0:
    total_cols += 1

print(total_cols)

