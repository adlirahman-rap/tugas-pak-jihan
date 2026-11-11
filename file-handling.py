# Membuat file 'catatan.txt' dan menulis teks ke dalamnya
with open("catatan.txt", "w") as file:
    file.write("Halo, ini baris pertama.\n")
    file.write("Belajar File Handling di Python.\n")

# Menambahkan baris baru tanpa menghapus tulisan sebelumnya
with open("catatan.txt", "a") as file:
    file.write("Ini adalah baris tambahan.\n")

# Membaca dan menampilkan seluruh isi 'catatan.txt' ke layar
with open("catatan.txt", "r") as file:
    isi = file.read()
    print(isi)
