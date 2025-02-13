import csv

file_name = "tubes.csv"


def load_data():
    try:
        with open(file_name, mode='r', newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader if len(row) == 2]
    except FileNotFoundError:
        return []


def save_data(data):
    with open(file_name, mode='w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def show_data(data):
    if not data:
        print("\n Data tidak ada!\n")
        return
    print("=" * 25)
    print("Daftar Kamus Gen Alpha: \n")
    for i, row in enumerate(data, 1):
        if len(row) == 2:
            kata, arti = row
            print(f"{i}.{kata} - {arti}")
    print("=" * 25)


def add_data(data):
    kata = input("Masukkan Kata: ")
    arti = input("Masukkan Makna: ")
    data.append([kata, arti])
    save_data(data)
    print("Entry Berhasil Ditambahkan!\n")


def edit_data(data):
    show_data(data)
    index = int(input("Masukkan Nomor Entry yang ingin diubah: ")) - 1
    if 0 <= index < len(data):
        kata = input(f"Masukkan Kata Baru ({data[index][0]}): ") or data[index][0]
        arti = input(f"Masukkan Makna dari Kata Baru ({data[index][1]}): ") or data[index][1]
        data[index] = [kata, arti]
        save_data(data)
        print("Entry Berhasil Diubah!")
    else:
        print("Entry Tidak Ada")


def delete_data(data):
    show_data(data)
    index = int(input("Masukan Nomor Entry Yang Ingin Dihapus: ")) - 1
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
        print("Entry Berhasil Dihapus!")
    else:
        print("Entry Tidak Ada")


def search_data(data):
    keyword = input("Masukkan Kata Kunci Pencarian: ").lower()
    hasil = [e for e in data if keyword in e[0].lower() or keyword in e[1].lower()]
    show_data(hasil)


def SelectionSort(data, posisi=0):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j][posisi].lower() < data[min_index][posisi].lower():
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


def sort_data(data):
    pilihan = input("Urutkan Entry Berdasarkan (1: Kata 2: Makna): ").lower()
    valid = True
    if pilihan == "1":
        data = SelectionSort(data, 0)
    elif pilihan == "2":
        data = SelectionSort(data, 1)
    else:
        print("Input Tidak Valid!")
        valid = False

    if valid:
        save_data(data)
        print("-" * 30)
        print("Entry Berhasil Diurukan!")
        print("Daftar Entry: ")
        for i, row in enumerate(data, 1):
            if len(row) == 2:
                kata, arti = row
                print(f"{i}.{kata}.{arti}")
        print("-" * 30)
    else:
        return 0


def main():
    data = load_data()
    while True:
        print("*" * 30)
        print("""
        Selamat Datang di Kamus Gen Alpha!
        Silahkan Memilih Opsi Berikut:

        1. Tambah Entry
        2. Ubah Entry
        3. Hapus Entry
        4. Cari Entry
        5. Urutkan Entry
        6. Tampilkan Entry
        0. Keluar
        """)
        print("*" * 30)
        pilihan = input("Pilih Menu : ")
        if pilihan == "1":
            add_data(data)
        elif pilihan == "2":
            edit_data(data)
        elif pilihan == "3":
            delete_data(data)
        elif pilihan == "4":
            search_data(data)
        elif pilihan == "5":
            sort_data(data)
        elif pilihan == "6":
            show_data(data)
        elif pilihan == "0":
            print("Keluar dari program............")
            break
        else:
            print("Pilihan Tidak Valid! Coba Lagi. \n")


if __name__ == "__main__":
    main()