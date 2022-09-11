
def Word_Counter(str_input):
    elements_list = [".", ",", "/", "\\", "[", "]", "{", "}", "!", "#", "&", "(",
                     ")", "*", "^", ":", ";", "\'", "\"", "<", ">", "|", "$", "%",
                     "~", "`", "@", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for el in elements_list:
        str_input = str_input.replace(el, " ")

    words_list = str_input.split()
    number_of_words = len(words_list)

    print("Number of Words: " + str(number_of_words))

str_input = input("Enter You're Desired String: ")

Word_Counter(str_input)