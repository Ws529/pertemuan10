list = {
    "Udin" : "081908102161", "Asep" : "085893756814"  
}
print("\nTampilkan kontak Udin :")
print(29*"=")
print(" {0:^2} |".format("Nama"), "Nomor Telepon")      
print("=============================")

# Tampilkan Kontak Udin
print(" {0:^2} |".format("Udin") ,list["Udin"],"\n")

# Tambah Kontak baru
list["Tio"] = "08774161531"

# Ubah kontak Asep dengan nomor baru
list["Asep"] = "085893756814"

# Tampilkan semua Nama 
print("Tampilan semua Nama :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")

for x in list.keys():
    print(" {0:^2} |".format(x))
print("\n")

# Tampilkan Semua Nomor 
print("Tampilan semua Nomor :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")

for x in list.values():
    print(" {0:^2} |".format(x))
print("\n")


# Tampilkan daftar Nama & Nomor
print("Tampilan daftar Nama & Nomor :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")

for x, y in list.items():
    print(" {0:^2} |".format(x), (y))
print("\n")

# Menghapus Kontak Asep
print("Menghapus Kontak Asep :")
print(29*"=")
del list["Asep"]

print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")

for x, y in list.items():
    print(" {0:^2} |".format(x), (y))
print("\n")