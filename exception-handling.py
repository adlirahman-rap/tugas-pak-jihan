try:
    angka = int(input("Masukkan angka pembagi: "))
    hasil = 100 / angka
except ZeroDivisionError:
    # Menangani khusus error jika dibagi dengan angka 0
    print("Error: Angka tidak boleh nol!")
except ValueError:
    # Menangani khusus error jika pengguna memasukkan huruf, bukan angka
    print("Error: Input harus berupa angka bulat!")
else:
    # Dijalankan jika tidak ada error
    print("Hasil pembagian adalah:", hasil)
finally:
    # Selalu dijalankan di akhir
    print("Proses perhitungan selesai.")
