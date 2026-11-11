# 1. Parent Class (Kelas Induk)
class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        print(f"Kendaraan {self.merk} keluaran tahun {self.tahun}")

# 2. Child Class (Kelas Anak) mewarisi Kendaraan
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_pintu):
        # Memanggil constructor milik Parent Class menggunakan super()
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu

    def klakson(self):
        print(f"Mobil {self.merk} membunyikan klakson: Tin! Tin!")

# Membuat objek dari Child Class
mobil_saya = Mobil("Toyota", 2024, 4)

# Memanggil method warisan dari Parent Class
mobil_saya.info()

# Memanggil method milik Child Class sendiri
mobil_saya.klakson()
