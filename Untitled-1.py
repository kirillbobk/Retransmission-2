def def_1(arg_1):
    list_1 = []
    list_2 = []
    
    for i in range(len(arg_1) - 1):
        a = arg_1[i] + arg_1[i + 1]
        list_1.append(a)
        b = arg_1[i] - arg_1[i + 1]
        list_2.append(b)
    return list_1,list_2
    
list_w = [1.0, 2.0, 3.0]

b = def_1(list_w)
print(b)