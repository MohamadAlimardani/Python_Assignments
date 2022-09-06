import random as ra
color=['red','blue','pink','brown','orange','purple','green','yellow','gray','black']
finall=ra.choice(color)
s_list=[]
w_list=[]

for i in range(len(finall)):
        s_list.append("_")
print(''.join(s_list)) 
while True:
    letter=input('enter letter one by one :')
    if finall.find(letter)==-1:
        w_list.append(letter)
        
    else:
        for i in range(len(finall)):
            if finall[i]==letter:
                s_list[i]=letter
            else:
                continue      
    print("".join(s_list))
    print(w_list)
