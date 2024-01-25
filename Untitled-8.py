def con_str(arg_str_list):
    if not arg_str_list:
        return ""  
    else:
        first_str = arg_str_list[0]
        rest_of_str = arg_str_list[1:]
        concatenated_str = first_str + " " + con_str(rest_of_str)
        return concatenated_str

str_list = ["a", "b", "c"]
result = con_str(str_list)
print("Result:", result)