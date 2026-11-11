from abc import ABC, abstractmethod

# 1. Membuat Abstract Class (Kerangka Dasar)
class Kendaraan(ABC):
    @abstractmethod
    def bergerak(self):
        pass  # Dikosongkan karena wajib diisi oleh kelas anak

# 2. Membuat Child Class yang mengisi detail method bergerak()
class Mobil(Kendaraan):
    def bergerak(self):
        print("Mobil melaju di jalan raya menggunakan roda.")

class Perahu(Kendaraan):
    def bergerak(self):
        print("Perahu berlayar di atas air.")

# Membuat objek dari kelas anak
mobil = Mobil()
perahu = Perahu()

mobil.bergerak()
perahu.bergerak()

# Jika memaksa membuat objek langsung dari Kendaraan(), Python akan Error!
