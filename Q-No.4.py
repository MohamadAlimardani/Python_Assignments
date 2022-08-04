
height = int(input("Enter you're Desired Height: "))
base = int(input("Enter you're Desired Base: "))

area = (height * base)/2
format_area = "{:.2f}".format(area)

print("Area of you're Triangle is: " , format_area)