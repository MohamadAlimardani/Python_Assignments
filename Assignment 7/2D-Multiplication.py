
rows, cols = int(input("Enter Rows: ")), int(input("Enter Columns: "))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(i * j , end = "\t")
    print(2 * "\n")
