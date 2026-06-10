def is_leap(a):
    if a<0 :
        raise ValueError
    elif a%400 == 0 or a%100 != 0 and a%4 == 0:
        return True
    else:
        return False