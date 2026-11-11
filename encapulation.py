class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal  # private attribute

    # getter (untuk mengambil/melihat data)
    def lihat_saldo(self):
        return self.__saldo

    # setter (untuk menambah data dengan validasi)
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    # setter (untuk mengurangi data dengan validasi)
    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")

# Membuat objek
akun = BankAccount(1000)

# Mengakses saldo lewat method (bukan langsung)
print("Saldo awal:", akun.lihat_saldo())
akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())
akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())
