# new names for functions, inputs and lists. wrote explanations of functions.

def drawing_number_concatenate(_count, _list, var_1, var_2, var_3, var_4, 
    var_5, var_6):
    """ this function concatenates the whole drawing number,
    for example 'K-20-1-100' """
    for i in range(0, _count):
        x = f"{var_1}-{var_2}-{var_3}-{var_4}{var_5}{var_6} - ".upper()
        _list.append(x)

    return _list

def drawing_name_part_1(_count, _list, _var):
    """ this function takes care of the first part of the drawing name, 
    for example the part 'BÖP' of 'BÖP 10' """
    for i in range(0, _count):
        _list.append(_var)

    return _list

def drawing_name_part_2(_count, _list, _var):
    """ this function takes care of the last part of the drawing name,
    for example the part '10' of 'BÖP 10' """
    for i in range(0, _count):
        _list.append(_var)
        _var += 1

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

discipline = input("Ange diciplin: ")
drawing_content = input("Ange ritningens innehåll: ")
drawing_category = input("Ange ritningens kategori: ")
house_number = input("Ange husnummer: ")
house_part = input("Ange husdel: ")
house_floor = input("Ange våning: ")
drawing_name = input("Ange ritnignens namn: ")
number_of_floors = int(input("Ange antal våningar: "))  

# empty lists
list_drawing_number_concatenate = [] 
list_drawing_name_part_1 = []
list_drawing_name_part_2 = []
list_drawing_name_concatenate = []
list_drawing_number_and_name_concatenate = []

# str to upper(), split()
drawing_name = drawing_name.upper().split()

# pop list to int / str
num = int(drawing_name.pop()); nam = drawing_name.pop()

# use func
list_drawing_number_concatenate = drawing_number_concatenate(
    number_of_floors, list_drawing_number_concatenate, discipline, 
    drawing_content, drawing_category, house_number, house_part, house_floor
    )
list_drawing_name_part_1 = drawing_name_part_1(
    number_of_floors, list_drawing_name_part_1, nam
    )
list_drawing_name_part_2 = drawing_name_part_2(
    number_of_floors, list_drawing_name_part_2, num
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