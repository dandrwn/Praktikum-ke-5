
print("Membuat Dictionary daftar kontak")

a = {'ari':"081267888", 
    'dina':"087677776",}
print(a.items())

print("\nMenampilkan ari")
print(a['ari'])

print("\nTambah kontak baru dengan nama Riko, nomor 087654544")
a['riko'] = "087654544"
print(a.items())

print("\nUbah kontak Dina dengan nomor baru 088999776")
a['dina'] = "088999776"
print(a.items())

print("\nTampilkan semua Nama")
for item in a.items():
    print(item[0])

print("\nTampilkan semua nomor")
for item in a.items():
    print(item[1])

print("\nTampilkan daftar Nama dan nomornya")
for item in a.items():
    print(item)

print("\nHapus kontak Dina")
del a['dina']
for item in a.items():
    print(item)