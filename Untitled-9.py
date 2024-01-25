def amount_num_file(arg_my_file):
    try:
        with open(arg_my_file, 'r') as file:
            nam = [int(row.strip()) for row in file.readlines()]
            sum = sum(nam)
            return sum
    except FileNotFoundError:
        print(f'File with the name ({arg_my_file}) not found.')
        return None
    except ValueError:
        print(f'File {arg_my_file} remove invalid values.')
        return None


my_file = 'nums.txt' 
результат = amount_num_file(my_file)

if результат is not None:
    print(f'Sum of numbers in the file {my_file}: {результат}')