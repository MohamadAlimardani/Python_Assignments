
import pyfiglet
import colorama
colorama.init()

start_orange = "\033[1;93m"
end_orange = "\033[0;0m"

def Chess_Board(n , m):
    nxm = n*m
    temp_n = n
    print_list = []
    result = []

    if (nxm)%2 == 0:
        size = ((nxm)/2)+1
        size = int(size)
        for i in range(size):
            print_list.append("$")

        x = "&".join(print_list)
        x = x.rstrip(x[-1])
        
        for el in x:
            result.append(el)

        for i in range(m-1):
            result.insert(n , "\n")
            n = n+temp_n+1
            
        result = "".join(result)

    else:
        size = ((nxm)/2)+1
        size = int(size)
        for i in range(size):
            print_list.append("$")

        x = "&".join(print_list)
        
        for el in x:
            result.append(el)

        for i in range(m-1):
            result.insert(n , "\n")
            n = n+temp_n+1
            
        result = "".join(result)

    finall = pyfiglet.figlet_format(result , font = "epic")
    print(start_orange + finall + end_orange)
    
rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))

Chess_Board(rows , columns)