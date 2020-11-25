from prettytable import PrettyTable
# Membuat list kosong untuk menampung
Mahasiswa = {}
stop = False
i = 0

# mengisi
while(not stop):
    nim = input("NIM : ")
    nama = input("Nama : ")
    uts = input("Nilai UTS : ")
    uas = input("Nilai UAS : ")
    tugas = input("Nilai Tugas : ")

    nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)

    Mahasiswa.append([nama, nim, tugas, uts, uas, nilai_akhir])

    lihat = input("lihat Data ? (Y/T): ")
    tambah= input("Tambah Data ? (Y/T): ")
    ubah= input("Ubah Data ? (Y/T): ")
    hapus= input("Hapus Data ? (Y/T): ")
    cari= input("Cari Data ? (Y/T): ")
    keluar= input("Keluar Data ? (Y/T): ")
    
    if tanya == "t":
        stop = True

x = PrettyTable()
i = 0

for data in Mahasiswa:
    i += 1
    x.field_names = ["No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"]
    x.add_row([i, data[0], data[1], data[2], data[3], data[4], data[5]])
print(x)