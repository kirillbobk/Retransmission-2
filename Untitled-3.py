def summar_arg(**arg_nam_1):
    res = None

    for i, j in arg_nam_1.items():
        if isinstance(j, (int, float)):
            if res is None:
                res = j
            else:
                res *= j
        elif isinstance(j, str):
            if arg_nam_1 is None:
                res = j
            else:
                res += j
        else:
            raise ValueError(f"Argument '{i}' data type unknown.")

    return res

try:
    res = summar_arg(nam_1 = 2, nam_2 = 3, nam_3 = 'w')
    print('Result:', res)
except ValueError as exc:
    print('Error:',exc)