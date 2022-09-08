
opr_list = ["+" , "-" , "*" , "/" , "^"]
sep_list , oprs = list() , list()

str_input = input("Enter You're Desired Expression: ")
numbers = str_input
oprs = str_input

for opr in opr_list:
    numbers = " ".join(numbers.split(opr))

numbers = numbers.split()

for i in range(len(numbers)):
    numbers[i] = float(numbers[i])

for i in range(10):
    oprs = " ".join(oprs.split(str(i)))

oprs = oprs.split()

for i , opr in enumerate(oprs):
    if opr == ".":
        del oprs[i]

i = -1
for x , ok in enumerate(numbers):
    try:
        i += 2
        numbers.insert(i , oprs[x])
    
    except:
        continue

while True:
    if len(numbers) != 1:
        for f , opr_pow in enumerate(numbers):
            if opr_pow == "^":
                numbers[f-1] = pow(numbers[f-1] , numbers[f+1])
                del numbers[f]
                del numbers[f]
        
        for j , opr_mult_div in enumerate(numbers):
            if opr_list[2] in numbers and opr_list[3] in numbers:
                first_mul_index = numbers.index(opr_list[2])
                first_div_index = numbers.index(opr_list[3])
                
                if first_mul_index < first_div_index:
                    numbers[first_mul_index-1] = numbers[first_mul_index-1] * numbers[first_mul_index+1]
                    del numbers[first_mul_index]
                    del numbers[first_mul_index]
                    
                    continue
                else:
                    numbers[first_div_index-1] = numbers[first_div_index-1] / numbers[first_div_index+1]
                    del numbers[first_div_index]
                    del numbers[first_div_index]
                    
                    continue

            elif opr_list[2] in numbers:
                first_mul_index = numbers.index(opr_list[2])
                
                numbers[first_mul_index-1] = numbers[first_mul_index-1] * numbers[first_mul_index+1]
                del numbers[first_mul_index]
                del numbers[first_mul_index]
                
                continue

            elif opr_list[3] in numbers:
                first_div_index = numbers.index(opr_list[3])
                
                numbers[first_div_index-1] = numbers[first_div_index-1] / numbers[first_div_index+1]
                del numbers[first_div_index]
                del numbers[first_div_index]
                
                continue
            
            else:
                break
        
        for j , opr_sum_sub in enumerate(numbers):
            if opr_list[0] in numbers and opr_list[1] in numbers:
                first_sum_index = numbers.index(opr_list[0])
                first_sub_index = numbers.index(opr_list[1])
                
                if first_sum_index < first_sub_index:
                    numbers[first_sum_index-1] = numbers[first_sum_index-1] + numbers[first_sum_index+1]
                    del numbers[first_sum_index]
                    del numbers[first_sum_index]
                    
                    continue
                else:
                    numbers[first_sub_index-1] = numbers[first_sub_index-1] - numbers[first_sub_index+1]
                    del numbers[first_sub_index]
                    del numbers[first_sub_index]
                    
                    continue

            elif opr_list[0] in numbers:
                first_sum_index = numbers.index(opr_list[0])
                
                numbers[first_sum_index-1] = numbers[first_sum_index-1] + numbers[first_sum_index+1]
                del numbers[first_sum_index]
                del numbers[first_sum_index]
                
                continue

            elif opr_list[1] in numbers:
                first_sub_index = numbers.index(opr_list[1])
                
                numbers[first_sub_index-1] = numbers[first_sub_index-1] - numbers[first_sub_index+1]
                del numbers[first_sub_index]
                del numbers[first_sub_index]
                
                continue
            
            else:
                break

    else:
        break

print(str_input + " = " + str(numbers[0]))