def append_fun(arg_mult):
    def append_fun_inside(elem):
        return (elem in arg_mult)
    return append_fun_inside

# Приклад використання функції
mult = {1, 2, 3, 4, 5}
rever_input_mult = append_fun(mult)

print(append_fun(3))  
print(append_fun(6))  