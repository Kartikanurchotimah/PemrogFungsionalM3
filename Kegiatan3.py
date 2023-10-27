random_list = [105, 3.1, 'Hello', 737, 'Pyhton', 2.7, 'Wolrd', 412, 5.5, 'AI']

is_float = lambda x: isinstance(x, float)
is_int = lambda x: isinstance(x, int)
is_str = lambda x: isinstance(x, str)

floats = list(filter(is_float, random_list))
ints = list(filter(is_int, random_list))
strings = list(filter(is_str, random_list))

def angka(num):
    ratusan = num // 100
    puluhan = (num % 100) // 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

int_dicts = list(map(angka, ints))

# Output
print("Data Float:", tuple(floats))
print("Data Int:")
for int_dict in int_dicts:
    print(int_dict)
print("Data String:", strings)