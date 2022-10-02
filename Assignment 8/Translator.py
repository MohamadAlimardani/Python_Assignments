
import os
import colorama
colorama.init()

start_red = "\033[1;91m"
end_red = "\033[0;0m"

start_grey = "\033[1;90m"
end_grey = "\033[0;0m"

def Dicts(list_of_words):
    eng_to_per_dict = dict()
    per_to_eng_dict = dict()


    for i in range(30):
        eng_to_per_dict[list_of_words[i]] = list_of_words[flag]



    for i in range(30):
        per_to_eng_dict[list_of_words[flag]] = list_of_words[i]


    return eng_to_per_dict, per_to_eng_dict

def extracting_words(file_name):
    with open(file_name, "r") as file:
        data = file .read()
        words = data.split("\n")
        return [each_string.lower() for each_string in words]

def translate():
    eng_dict, per_dict = Dicts(extracting_words("Words_Translator.txt"))
    
    os.system("cls")
    str_sample = input("\nEnter You're Desired Sentence: ").lower()
    temp_per = str_sample.split()
    temp_eng = str_sample.split()

    flag_per = 0
    for i, ele in enumerate(temp_per):
        if ele in per_dict:
            temp_per[i] = start_red + per_dict[ele].upper() + end_red
            flag_per += 1
            continue
        temp_per[i] = start_grey + ele.capitalize() + end_grey 
    
    per_translate = " ".join(temp_per)
    
    flag_eng = 0
    for i, ele in enumerate(temp_eng):
        if ele in eng_dict:
            temp_eng[i] = start_red + eng_dict[ele].upper() + end_red
            flag_eng += 1
            continue
        temp_eng[i] = start_grey + ele.capitalize() + end_grey
    
    eng_translate = " ".join(temp_eng)

    return flag_per, flag_eng, per_translate, eng_translate

def show_result():
    if per_flag == eng_flag:
        os.system("cls")
        print(f"\nEnglish Translate: {per_translate}\n\nPersian Translate: {eng_translate}\n")

    elif per_flag > eng_flag:
        os.system("cls")
        print(f"\nEnglish Translate: {per_translate}\n")

    elif per_flag < eng_flag:
        os.system("cls")
        print(f"\nPersian Translate: {eng_translate}\n")

per_flag, eng_flag, per_translate, eng_translate = translate()

show_result()
