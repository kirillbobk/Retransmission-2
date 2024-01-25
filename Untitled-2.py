def def_1(arg_1):
    dict_1 = {}
    for i in arg_1:
        if (i != 0):
            dict_1[int(i)] = i
        else:
            dict_1[int(i)] = i
    return dict_1

n = ['0', '1', '2']
m = ['1', '2', '3']
a = def_1(n)
b = def_1(m)
print(a)
print(b)

    #if (i != '0'):
            #dict_1 = dict(([i, int(i)]))
        #return i   #Создать 