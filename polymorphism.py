class Kucing:
    def bersuara(self):
        print("Meong... Meong...")

class Anjing:
    def bersuara(self):
        print("Guk... Guk...")

class Sapi:
    def bersuara(self):
        print("Mooo...")

# Membuat daftar objek dari class yang berbeda-beda
hewan_peliharaan = [Kucing(), Anjing(), Sapi()]

# Memanggil method bersuara() dengan cara yang sama
for hewan in hewan_peliharaan:
    hewan.bersuara()

