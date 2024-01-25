def gener_list(arg_nam):
    if arg_nam < 0:
        return []
    else:
        front_list =gener_list(arg_nam - 1)
        cur_item = arg_nam
        return front_list + [cur_item]

enter_num = int(input('Enter the number of additional numbers: '))
answer = gener_list(enter_num)
print('Answer:', answer)