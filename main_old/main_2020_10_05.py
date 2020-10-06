# new func 'name' replaces old var num and nam, argument variables replace input variables, work width drawing_name_part_1 / 2, new floor counter

from sys import argv

(script, discipline, drawing_content, drawing_category, house_number,
house_part, house_floor, drawing_name, number_of_floors) = argv

number_of_floors = int(number_of_floors)
house_floor = int(house_floor)


def drawing_number_concatenate(_count, var_1, var_2, var_3, var_4, 
    var_5, var_6):
    """ this function concatenates the whole drawing number,
    for example 'K-20-1-100' """
    list_1 = []
    list_2 = []
    list_3 = []
    for i in range(0, _count):
        x = f"{var_1}-{var_2}-{var_3}-{var_4}{var_5}".upper()
        list_1.append(x)

    for i in range(0, _count):
        list_2.append(var_6)
        var_6 += 1
    
    for i in range(0, _count):
        a = list_1.pop(0)
        b = str(list_2.pop(0))
        list_3.append(f"{a + b} - ")

    return list_3

def drawing_name_part_1(_count, _list, _var):
    """ this function takes care of the first part of the drawing name, 
    for example the part 'BÖP' of 'BÖP 10' """
    i = _var.upper().split()
    j = i.pop(0)
    
    for i in range(0, _count):
        _list.append(j)

    return _list

def drawing_name_part_2(_count, _list, _var):
    """ this function takes care of the last part of the drawing name,
    for example the part '10' of 'BÖP 10' """
    i = _var.upper().split()
    j = int(i.pop())

    for i in range(0, _count):
        _list.append(j)
        j += 1

    return _list

def drawing_name_concatenate(_count, list_1, list_2, list_3):
    """ this function concatenates drawing_name_part_1 and drawing_name_part_2,
    for example the part 'BÖP' and '10' concatenates to 'BÖP 10' """
    for i in range(0, _count):
        x = list_1.pop(0)
        y = list_2.pop(0)
        z = f"{x} {y}"
        list_3.append(z)

    return list_3

def drawing_number_and_name_concatenate(_count, list_1, list_2, list_3):
    """ this function concatenates  drawing_number_concatenate and 
    drawing_name_concatenate,
    for example the part 'BÖP' and '10' concatenates to 'BÖP 10' """
    for i in range(0, _count):
        x = list_1.pop(0)
        y = list_2.pop(0)
        z = f"{x}{y}"
        list_3.append(z)

    return list_3

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