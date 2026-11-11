# Cara 1: Mengimpor seluruh isi module
import matematika

print(matematika.tambah(5, 3))  # Output: 8
print(matematika.PI)            # Output: 3.14

# Cara 2: Mengimpor dengan nama singkatan (alias 'as')
import matematika as mtk

print(mtk.kali(4, 2))           # Output: 8

# Cara 3: Mengimpor fungsi atau variabel tertentu saja
from matematika import tambah

print(tambah(10, 5))            # Output: 15
