import random

welcome_message = ' Welcome bro '
lokasi_air = random.randint(1,4)

print ('*****************')
print (f'**{welcome_message}**')
print ('*****************')

nama = input('masukkan nama anda : ')

bentuk_gelas = '|___|'
gelas_kosong = [bentuk_gelas] * 4
gelas_isi = gelas_kosong.copy()

gelas_isi[lokasi_air - 1] = '|███|'



print()
print(f'Hallo {nama} coba perhatikan Gelas dibawah ini :')
print(''.join(gelas_kosong))
print()

pilihan_user = int(input('Lokasi air berada di gelas no berapa? : ' ))
print()

while True :
    konfirmasi = input('apakah kamu yakin dengan pilihanmu Y/N? : ')

    if konfirmasi == 'N' :
        print('Mohon ulangi program!!! untuk mengulang pilihan')
        exit()
    elif konfirmasi == 'Y' :
        break      
    else:
        print('Perhatikan huruf besarnya dan cuman menerima jawaban Y/N')
        continue
    

if pilihan_user == lokasi_air :
    print (f'SELAMAT KAMU MENANG!!! Lokasi air berada di gelas no : {lokasi_air}')
    print (''.join(gelas_isi))
elif pilihan_user > 4 :
    print (f'KOCAK!!!! Gelas cuman 4 Boss, gelas yang berisi air ada di gelas no : {lokasi_air}')
    print (''.join(gelas_isi))
else:
    print (f'Kamu kalah!!!! lokasi air berada di gelas no : {lokasi_air}')
    print(''.join(gelas_isi))