# import of functions

from sys import argv
from func import *

(script, discipline, drawing_content, drawing_category, house_number,
house_part, house_floor, drawing_name, number_of_floors) = argv

number_of_floors = int(number_of_floors)
house_floor = int(house_floor)

# empty lists
list_drawing_number_concatenate = [] 
list_drawing_name_part_1 = []
list_drawing_name_part_2 = []
list_drawing_name_concatenate = []
list_drawing_number_and_name_concatenate = []

list_drawing_number_concatenate = drawing_number_concatenate(number_of_floors,
    discipline, drawing_content, drawing_category, house_number, house_part,
    house_floor    
    )

list_drawing_name_part_1 = drawing_name_part_1(
    number_of_floors, list_drawing_name_part_1, drawing_name
    )

list_drawing_name_part_2 = drawing_name_part_2(
    number_of_floors, list_drawing_name_part_2, drawing_name
    )
list_drawing_name_concatenate = drawing_name_concatenate(
    number_of_floors, list_drawing_name_part_1, list_drawing_name_part_2,
    list_drawing_name_concatenate
    )
list_drawing_number_and_name_concatenate = drawing_number_and_name_concatenate(
    number_of_floors, list_drawing_number_concatenate, 
    list_drawing_name_concatenate, list_drawing_number_and_name_concatenate
    )

for i in range (0, number_of_floors):
    print(list_drawing_number_and_name_concatenate.pop(0))