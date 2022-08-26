
bakery_line = ["Ali", "Atefe", "Reza", "Homa", "Amir", "Fatemeh"]

print("\n\n")

first_zhen_khook_name = input("Enter You're Trash Name: ")
first_zhen_khook_spot = int(input("Enter Where You wanna Be Morafah e Bi Dard: "))
print("\n")
second_zhen_khook_name = input("Enter You're Trash Name: ")
second_zhen_khook_spot = int(input("Enter Where You wanna Be Morafah e Bi Dard: "))
print("\n")
third_zhen_khook_name = input("Enter You're Trash Name: ")
third_zhen_khook_spot = int(input("Enter Where You wanna Be Morafah e Bi Dard: "))
print("\n")
bakery_line.insert(first_zhen_khook_spot-1, first_zhen_khook_name)
bakery_line.insert(second_zhen_khook_spot-1, second_zhen_khook_name)
bakery_line.insert(third_zhen_khook_spot-1, third_zhen_khook_name)

print("All The People That Are in The Bakery Line:\n\n" , bakery_line , "\n\n")
