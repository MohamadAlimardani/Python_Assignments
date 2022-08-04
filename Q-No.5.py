
height = float(input("Enter you're Desired Height: "))
radius = float(input("Enter you're Desired Radius: "))

pi = 3.1415

volume = pi * (radius ** 2) * height
format_volume = "{:.2f}".format(volume)

lateral_surface = 2 * pi * radius * height
format_lateral_surface = "{:.2f}".format(lateral_surface)

surface_area = lateral_surface + (2 * pi * (radius ** 2))
format_surface_area = "{:.2f}".format(surface_area)

print("Volume of the Cylinder is: " , format_volume , "\nLateral Surface of the Cylinder is: " , format_lateral_surface , "\nSurface Area of the Cylinder is: " , format_surface_area)

