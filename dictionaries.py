print("dictionaris_create\n")
# Membuat Dictionaries untuk menyimpan informasi biodata seseorang (nama dan umur)
firstPerson = {
   "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Untuk mengakses item pada Dictionaries bisa menggunakan 2 cara
# Cara pertama
print(firstPerson['first_name']) # Hana
# Cara kedua dengan method "get"
print(firstPerson.get('age')) # 10

# Untuk mendapatkan semua "keys" dari Dictionaries
print(firstPerson.keys()) # dict_keys(['name', 'age'])

# Untuk mendapatkan semua "values" dari Dictionaries
print(firstPerson.values()) # dict_values(['Hana', 'Malika', 10, 12])


print("\ndictionaries add item\n")
firstPerson = {
   "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Menambahkan item ke dalam Dictionaries
# Menambahkan item berat bedan (weight) ke dalam firstPerson
firstPerson['weight'] = 12
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 10, 'weight': 12}

print("\ndictionaries update item\n")
firstPerson = {
   "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Ada 2 cara untuk mengubah atau mengupdate sebuah value dari item pada Dictionaries

# Cara Pertama
firstPerson['age'] = 15

# Cara Kedua dengan method "update"
# Jika kita menggunakan cara ini, ketika item yang di update berdasarkan key (age) ditemukan,
# maka akan diupdate.
# Namun jika item belum ada, maka otomatis akan menambahkan item baru
firstPerson.update({"age": 15})
firstPerson.update({"hair_color": "black"})
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 15, 'hair_color': 'black'}

print("\n dictionaries delete item\n")
firstPerson = {
   "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Untuk menghapus item dari Dictionaries, kita bisa menggunakan method "pop"
# Kita wajib menambahkan nama "key" jika menggunakan method "pop"
firstPerson.pop("age")
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika'}

# Untuk menghapus semua item, kita bisa menggunakan method "clear"
firstPerson.clear()
print(firstPerson) # {}

