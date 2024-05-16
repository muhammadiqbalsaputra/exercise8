import modul_exercise7 as modul
while True:
    modul.tampilan()
    pilihan = int(input('Masukan Pilihan : '))

    if pilihan == 1:
        modul.insert()

    if pilihan == 2:
        modul.delete()
    
    if pilihan == 3:
        modul.total()

    if pilihan == 4:
        print('='*25)
        print('Terimakasih Telah Mencoba')
        print('='*25)
        exit()