def gener_unpai():
    nam = 1
    while True:
        yield nam
        nam += 2

unpai_num_gen = gener_unpai()
non_numbers = [next(i) for i in range(20)]

print(non_numbers)