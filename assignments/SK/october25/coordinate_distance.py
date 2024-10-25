import math

longitude_1 = float(input("Input the longitude of the first coordinate: "))
latitude_1 = float(input("Input the latitude of the first coordinate: "))
longitude_2 = float(input("Input the longitude of the second coordinate: "))
latitude_2 = float(input("Input the latitude of the second coordinate: "))
radius = 6371.01

distance_part_1 = radius * math.acos(math.sin(longitude_1)) * math.sin(longitude_2)
distance_part_2 = math.cos(longitude_1) * math.cos(longitude_2) * math.cos(latitude_1 - latitude_2)

distance = distance_part_1 + distance_part_2

print(f"The distance between the 2 coordinates is {distance: .2f}km")