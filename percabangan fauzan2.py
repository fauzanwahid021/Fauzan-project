# variabel dan tipe data
nama_mhs = input("Masukkan Nama Mahasiswa:")
nalgoritma = int(input("Masukkan Nilai Algoritma:"))
nagama = int(input("Masukkan Nilai Agama:"))
nbasisdata = int(input("Masukkan Nilai Basis Data:"))
npancasila = int(input("Masukkan Nilai Pancasila:"))
nbhsinggris = int(input("Masukkan Nilai Bhs Inggris:"))
nbhsindo = int(input("Masukkan Nilai Bhs Indo:"))
nakutansi = int(input("Masukkan Nilai Akutansi:"))
rata_rata = (nalgoritma + nagama + nbasisdata + npancasila + nbhsinggris + nbhsindo + nakutansi) / 7
# print(rata_rata)

# penentuan Nilai
if rata_rata>=90 and rata_rata<=100:
    # kondisi jika terpenuhi
    # maka
    
    print("Nilai: A")
elif rata_rata >=80 and rata_rata<=90:
    print("Nilai: B")        
elif rata_rata >=60 and rata_rata<=70:
    print("Nilai: C")
elif rata_rata >=50 and rata_rata<=60:
    print("Nilai: D")
else:
    # cukup menampilkan hasil
    # maka
    print("Rata rata Lebih dari 100 atau dibawah 50")     