# FUNC FOR VAR RIT_NA

def rit_na_str(_count, _list, _var):
    for i in range(0, _count):
        _list.append(_var)
    return _list

def rit_na_int(_count, _list, _var):
    for i in range(0, _count):
        _list.append(_var)
        _var += 1
    return _list

def rit_na_conc(_count, list_1, list_2, list_3):
    for i in range(0, _count):
        x = list_1.pop(0)
        y = list_2.pop(0)
        z = f"{x} {y}"
        list_3.append(z)
    return list_3

#####################################################