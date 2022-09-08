
chr_list , temp = list() , list()
while True:
    str_input = input("Enter You're Desired Word/Sentence: ")

    for chr in str_input:
        chr_list.append(chr)
        temp.append(chr)

    chr_list.reverse()

    if chr_list == temp:
        print("The Given Word is Palindrome.")

    else:
        print("The Given Word is not Palindrome.")