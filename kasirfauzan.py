print("================================")
print("     APLIKASI KASIR RESTORAN")
print("================================")

total = 0

while True:
    print("\n===== MENU MAKANAN =====")
    print("1. Bebek Goreng  - Rp25.000")
    print("2. Mie Goreng     - Rp15.000")
    print("3. Ayam Bakar  - Rp20.000")
    print("4. Sate Kambing    - Rp30.000")
    print("5. Bakso        - Rp18.000")
    print("0. Selesai Memilih")

    pilihan = int(input("\nPilih menu (0-5): "))

    if pilihan == 0:
        break

    elif pilihan == 1:
        nama = "Bebek Goreng"
        harga = 25000

    elif pilihan == 2:
        nama = "Mie Goreng"
        harga = 15000

    elif pilihan == 3:
        nama = "Ayam Bakar"
        harga = 20000

    elif pilihan == 4:
        nama = "Sate Kambing"
        harga = 30000

    elif pilihan == 5:
        nama = "Bakso"
        harga = 18000

    else:
        print("Pilihan tidak tersedia!")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))

    if jumlah <= 0:
        print("Jumlah pesanan harus lebih dari 0!")
        continue

    subtotal = harga * jumlah
    total += subtotal

    print("Menu:", nama)
    print("Subtotal: Rp", subtotal)
    print("Total sementara: Rp", total)

# Menghitung diskon
if total > 200000:
    diskon = 20
else:
    diskon = 0

potongan = total * diskon / 100
total_bayar = total - potongan

# Menampilkan struk
print("\n================================")
print("       STRUK PEMBAYARAN")
print("================================")
print("Total Belanja : Rp", total)
print("Diskon        :", diskon, "%")
print("Potongan      : Rp", int(potongan))
print("Total Bayar   : Rp", int(total_bayar))
print("================================")
print("        TERIMA KASIH!")
print("================================")