def decode_message(message, key):
    """
    Mendekode pesan berdasarkan kunci yang diberikan.
    """
    if key == "key1":
        # Kondisi: Jika kunci adalah "key1"
        # Aksi: Ubah pesan menjadi huruf besar
        decoded_message = message.upper()
    elif key == "key2":
        # Kondisi: Jika kunci adalah "key2"
        # Aksi: Balikkan urutan karakter dalam pesan
        decoded_message = message[::-1]
    elif key == "key3":
        # Kondisi: Jika kunci adalah "key3"
        # Aksi: Geser setiap karakter mundur satu posisi (contoh dekode Caesar cipher)
        decoded_message = "".join([chr(ord(char) - 1) for char in message])
    else:
        # Kondisi: Jika kunci tidak valid
        # Aksi: Berikan pesan kesalahan
        decoded_message = "Kunci tidak valid. Silakan gunakan key1, key2, atau key3."
    return decoded_message

# Meminta input dari pengguna
message = input("Masukkan pesan yang akan didekode: ")
key = input("Masukkan kunci dekode (key1, key2, atau key3): ")

# Memanggil fungsi dekode dan menampilkan hasilnya
decoded_message = decode_message(message, key)
print("Pesan yang telah didekode: ", decoded_message)
