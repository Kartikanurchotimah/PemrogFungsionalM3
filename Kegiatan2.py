def konversi(m):
    def hari(h):
        def jam(j):
            def menit(mn):
                return m * 7 * 24 * 60 + h * 24 * 60 + j * 60 + mn
            return menit
        return jam
    return hari

# Data kegiatan
data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

konversi_data = []

for item in data:
    # Pisahkan data menjadi minggu, hari, jam, dan menit
    data_split = item.split()
    m = int(data_split[0]) if "minggu" in item else 0
    h = int(data_split[2]) if "hari" in item else 0
    j = int(data_split[4]) if "jam" in item else 0
    mn = int(data_split[6]) if "menit" in item else 0
    
    konvert = konversi(m)(h)(j)(mn)
    konversi_data.append([m, h, j, mn])

hasil_filter = [list(map(str, filter(lambda x: isinstance(x, int), sublist))) for sublist in konversi_data]

# Menampilkan hasil
for item in hasil_filter:
    print(item)