#n1
lst = [None, None, 1, [], (), {}, None]
lst2 = []
def de_none(lst):
    for val in lst:
        if val != None:
            lst2.append(val)
    return lst2
print(de_none(lst))
