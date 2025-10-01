nama = input("Masukkan nama produk: ")
jenis = input("Jenis produk (Elektronik/Pakaian/Makanan/Kosmetik): ")
harga = int(input("Harga produk (Rp): "))
penjualan = int(input("Jumlah unit terjual: "))

if jenis == "Elektronik":
    kategori_jenis = "Elektronik"
elif jenis == "Pakaian":
    kategori_jenis = "Pakaian"
elif jenis == "Makanan":
    kategori_jenis = "Makanan"
elif jenis == "Kosmetik":
    kategori_jenis = "Kosmetik"
else:
    kategori_jenis = "Lainnya"


if harga > 100000:
    kategori_harga = "Premium"
elif harga >= 50000:
    kategori_harga = "Menengah"
else:
    kategori_harga = "Terjangkau"


if penjualan >= 100:
    kategori_penjualan = "Best Seller"
elif penjualan >= 50:
    kategori_penjualan = "Populer"
else:
    kategori_penjualan = "Normal"


print("\n=== HASIL KATEGORI PRODUK ===")
print("Nama Produk       :", nama)
print("Jenis Produk      :", kategori_jenis)
print("Kategori Harga    :", kategori_harga)
print("Kategori Penjualan:", kategori_penjualan)