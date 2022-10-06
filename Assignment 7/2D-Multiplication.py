
rows_cols = int(input("Enter a Number \'?x?\': "))

for i in range(1, rows_cols + 1):
    for j in range(1, rows_cols + 1):
        print(i * j , end = "\t")
    print(2 * "\n")
