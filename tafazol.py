tafazol = 0

def game (number):

    a = number // 10
    b = number % 10

    if a > b:
        tafazol = a -  b
        
    elif  a < b:
        tafazol =  b -  a
        
    else:
        tafazol = 0

    return tafazol
