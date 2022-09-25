
rows_cols = int(input("Enter a Number \'?x?\': "))
m , n = 1 , 1

for i in range(rows_cols):
    for j in range(rows_cols):
        print(m * n , end = "\t")
        n += 1
    n = 1
    m += 1
    print(2 * "\n")