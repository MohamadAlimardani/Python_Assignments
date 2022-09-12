
import pyfiglet
import colorama
colorama.init()

start_grey = "\033[1;90m"
end_grey = "\033[0;0m"

def Chess_Board(n , m):
    nxm = n*m
    range_n = int(n/2)
    temp_n = n
    print_list = []
    result = []
    str_result = ""

    if (nxm)%2 == 0:
        if n%2 == 0:
            for i in range(m):
                print()
                str_result = ""
                
                for j in range(range_n):
                    if i%2 == 0:
                        str_result += "$&"
                    
                    else:
                        str_result += "&$"
            
                finall = pyfiglet.figlet_format(str_result , font = "banner3-d")
                print(start_grey + finall + end_grey)

        else:
            for i in range(m):
                print()
                str_result = ""
                
                for j in range(range_n+1):
                    if i%2 == 0:
                        str_result += "$&"
                    
                    else:
                        str_result += "&$"
                
                str_result = str_result.rstrip(str_result[-1])
                
                finall = pyfiglet.figlet_format(str_result , font = "banner3-d")
                print(start_grey + finall + end_grey)

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

        finall = pyfiglet.figlet_format(result , font = "banner3-d")
        print(start_grey + finall + end_grey)

rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))

Chess_Board(rows , columns)
