
height = int(input("Enter you're Desired Height: "))
base = int(input("Enter you're Desired Base: "))

surface = (height * base)/2
format_surface = "{:.2f}".format(surface)

print("Area of you're Triangle is: " , format_surface)