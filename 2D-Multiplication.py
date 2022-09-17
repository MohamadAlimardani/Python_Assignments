
rows , cols = 10 , 10
m , n = 1 , 1
x = [[0] * cols] * rows

for i in range(rows):
    for j in range(cols):
        # print(f"i = {i} , j = {j}")
        # print(f"m = {m} , n = {n}")
        x[i][j] = m * n
        print(x[i][j] , end = " ")
        n += 1
    n = 1
    m += 1
    print()

# for i in range(rows):
#     for j in range(cols):
#         print(x[i][j] , end = " ")

#     print()