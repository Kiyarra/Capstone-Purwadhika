listMurid = [
    {
        'nama': 'Kiara',
        'ID': 110,
        'alamat': 'Kemang',
        'Nilai' : 80,
    },
    {
        'nama': 'Oceano',
        'ID': 111,
        'alamat': 'Bintaro',
        'Nilai' : 85,
    },
    {
        'nama': 'Oktavia',
        'ID': 112,
        'alamat': 'Pendurenan',
        'Nilai' : 70
    },
    {
        'nama': 'Haris',
        'ID': 113,
        'alamat': 'Mampang',
        'Nilai' : 89,
    },
    {
        'nama': 'Malik',
        'ID': 114,
        'alamat': 'Pendurenan',
        'Nilai' : 75
    }

]
  
def daftarMurid () :
    print('Daftar Murid\n')
    print('Index\t| Nama  \t| ID\t| Alamat\t| Nilai')
    for i in range(len(listMurid)) :
        print('{}\t| {}  \t| {}\t| {}\t| {}'.format(i,listMurid[i]['nama'],listMurid[i]['ID'],listMurid[i]['alamat'],listMurid[i]['Nilai']))

def edit_menu () :
    daftarMurid()
    while True :
        menuEdit = int(input('''
                
                Menu Edit :
                1. Menambah Murid
                2. Menghapus Murid
                3. Mengubah Data Murid
                4. Kembali ke Menu Utama

                Masukkan angka Menu yang ingin dijalankan : '''))
            
        if menuEdit == 1:  
            namaMurid = input('Masukkan Nama Murid : ')
            studentID = int(input('Masukkan Student ID : '))
            alamatMurid = input('Masukkan Alamat Murid : ')
            nilaiMurid = int(input('Masukkan Nilai Murid: '))
            listMurid.append({
                        'nama': namaMurid,
                        'ID': studentID,
                        'alamat': alamatMurid,
                        'Nilai' : nilaiMurid
                        })
            daftarMurid()
        elif menuEdit == 2 :
            daftarMurid()
            indexMurid = int(input('Masukan Index Murid Yang Ingin di Hapus : '))
            del listMurid[indexMurid]
            daftarMurid()
        elif menuEdit == 3:
            daftarMurid()
            input_index = int(input('Masukan Index Yang ingin dirubah : '))
            if input_index == 0 :
                Data1 = int(input('''
                        Edit Data :
                        1. Nama
                        2. ID
                        3. Alamat
                        4. Nilai
                        5. Kembali Ke Menu Utama
                                        
                        Masukan Angka yang Ingin di Jalankan: '''))
                    
                if Data1 == 1 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[0]['nama'],listMurid[0]['ID'],listMurid[0]['alamat'],listMurid[0]['Nilai'])
                    Nama_1 = input('Silahkan Masukan Nama Yang Ingin di Rubah : ')
                    listMurid[0]['nama'] = Nama_1
                    daftarMurid()
                elif Data1 == 2 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[0]['nama'], listMurid[0]['ID'],listMurid[0]['alamat'],listMurid[0]['Nilai'])
                    id_1 = int(input('Silahkan Masukan ID Yang Ingin di Rubah : '))
                    listMurid[0]['ID'] = id_1
                    daftarMurid()
                elif Data1 == 3 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[0]['nama'],listMurid[0]['ID'],listMurid[0]['alamat'],listMurid[0]['Nilai'])
                    alamat_1 = input('Silahkan Masukan Alamat Yang Ingin di Rubah : ')
                    listMurid[0]['alamat'] = alamat_1
                    daftarMurid()
                elif Data1 == 4 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[0]['nama'],listMurid[0]['ID'],listMurid[0]['alamat'],listMurid[0]['Nilai'])
                    Nilai_1 = int(input('Silahkan Masukan Nilai Yang Ingin di Rubah : '))
                    listMurid[0]['Nilai'] = Nilai_1
                    daftarMurid()
                else :
                    print(edit_menu)
            elif input_index == 1 :
                Data2 = int(input('''
                        Edit Data :
                        1. Nama
                        2. ID
                        3. Alamat
                        4. Nilai
                        5. Kembali Ke Menu Utama
                                        
                        Masukan Angka yang Ingin di Jalankan: '''))
                if Data2 == 1 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[1]['nama'],listMurid[1]['ID'],listMurid[1]['alamat'],listMurid[1]['Nilai'])
                    Nama_2 = input('Silahkan Masukan Nama Yang Ingin di Rubah : ')
                    listMurid[1]['nama'] = Nama_2
                    print('Daftar Murid\n')
                    print('Index\t| Nama  \t| ID\t| Alamat\t| Nilai')
                    for i in range(len(listMurid)) :
                            print('{}\t| {}  \t| {}\t| {}\t| {}'.format(i,listMurid[i]['nama'],listMurid[i]['ID'],listMurid[i]['alamat'],listMurid[i]['Nilai']))
                elif Data2 == 2 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[1]['nama'], listMurid[1]['ID'],listMurid[1]['alamat'],listMurid[1]['Nilai'])
                    id_2 = int(input('Silahkan Masukan ID Yang Ingin di Rubah : '))
                    listMurid[1]['ID'] = id_2
                    daftarMurid()
                elif Data2 == 3 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[1]['nama'],listMurid[1]['ID'],listMurid[1]['alamat'],listMurid[1]['Nilai'])
                    alamat_2 = input('Silahkan Masukan Alamat Yang Ingin di Rubah : ')
                    listMurid[1]['alamat'] = alamat_2
                    daftarMurid()
                elif Data2 == 4 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[1]['nama'],listMurid[1]['ID'],listMurid[1]['alamat'],listMurid[1]['Nilai'])
                    Nilai_2 = int(input('Silahkan Masukan Nilai Yang Ingin di Rubah : '))
                    listMurid[1]['Nilai'] = Nilai_2
                    print('Daftar Murid\n')
                    print('Index\t| Nama  \t| ID\t| Alamat\t| Nilai')
                    daftarMurid()
                else :
                    print(menuEdit)          
            elif input_index == 2 :
                Data3 = int(input('''
                        Edit Data :
                        1. Nama
                        2. ID
                        3. Alamat
                        4. Nilai
                        5. Kembali Ke Menu Utama
                                        
                        Masukan Angka yang Ingin di Jalankan: '''))
                if Data3 == 1 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[2]['nama'],listMurid[2]['ID'],listMurid[2]['alamat'],listMurid[2]['Nilai'])
                    Nama_3 = input('Silahkan Masukan Nama Yang Ingin di Rubah : ')
                    listMurid[2]['nama'] = Nama_3
                    daftarMurid()
                elif Data3 == 2 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[2]['nama'], listMurid[2]['ID'],listMurid[2]['alamat'],listMurid[2]['Nilai'])
                    id_3 = int(input('Silahkan Masukan ID Yang Ingin di Rubah : '))
                    listMurid[2]['ID'] = id_3
                    daftarMurid()
                elif Data3 == 3 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[2]['nama'],listMurid[2]['ID'],listMurid[2]['alamat'],listMurid[2]['Nilai'])
                    alamat_3 = input('Silahkan Masukan Alamat Yang Ingin di Rubah : ')
                    listMurid[2]['alamat'] = alamat_3
                    daftarMurid()
                elif Data3 == 4 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[2]['nama'],listMurid[2]['ID'],listMurid[2]['alamat'],listMurid[2]['Nilai'])
                    Nilai_3 = int(input('Silahkan Masukan Nilai Yang Ingin di Rubah : '))
                    listMurid[2]['Nilai'] = Nilai_3
                    daftarMurid()
                else :
                    print(menuEdit)  
            elif input_index == 4 :
                Data4 = int(input('''
                        Edit Data :
                        1. Nama
                        2. ID
                        3. Alamat
                        4. Nilai
                        5. Kembali Ke Menu Utama
                                        
                        Masukan Angka yang Ingin di Jalankan: '''))
                if Data4 == 1 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[3]['nama'],listMurid[3]['ID'],listMurid[3]['alamat'],listMurid[3]['Nilai'])
                    Nama_4 = input('Silahkan Masukan Nama Yang Ingin di Rubah : ')
                    listMurid[3]['nama'] = Nama_4
                    daftarMurid()
                elif Data4 == 2 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[3]['nama'], listMurid[3]['ID'],listMurid[3]['alamat'],listMurid[3]['Nilai'])
                    id_4 = int(input('Silahkan Masukan ID Yang Ingin di Rubah : '))
                    listMurid[3]['ID'] = id_4
                    daftarMurid()
                elif Data4 == 3 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[3]['nama'],listMurid[3]['ID'],listMurid[3]['alamat'],listMurid[3]['Nilai'])
                    alamat_4 = input('Silahkan Masukan Alamat Yang Ingin di Rubah : ')
                    listMurid[3]['alamat'] = alamat_4
                    daftarMurid()
                elif Data4 == 3 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[3]['nama'],listMurid[3]['ID'],listMurid[3]['alamat'],listMurid[3]['Nilai'])
                    Nilai_4 = int(input('Silahkan Masukan Nilai Yang Ingin di Rubah : '))
                    listMurid[3]['Nilai'] = Nilai_4
                    daftarMurid()
                else :
                    print(menuEdit)  
            elif input_index == 4 :
                Data5 = int(input('''
                        Edit Data :
                        1. Nama
                        2. ID
                        3. Alamat
                        4. Nilai
                        5. Kembali Ke Menu Utama
                                        
                        Masukan Angka yang Ingin di Jalankan: '''))
                if Data5 == 1 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[4]['nama'],listMurid[4]['ID'],listMurid[4]['alamat'],listMurid[4]['Nilai'])
                    Nama_5 = input('Silahkan Masukan Nama Yang Ingin di Rubah : ')
                    listMurid[4]['nama'] = Nama_5
                    daftarMurid()
                elif Data5 == 2 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[4]['nama'], listMurid[4]['ID'],listMurid[4]['alamat'],listMurid[4]['Nilai'])
                    id_5 = int(input('Silahkan Masukan ID Yang Ingin di Rubah : '))
                    listMurid[4]['ID'] = id_5
                    daftarMurid()
                elif Data5 == 3 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[4]['nama'],listMurid[4]['ID'],listMurid[4]['alamat'],listMurid[4]['Nilai'])
                    alamat_5 = input('Silahkan Masukan Alamat Yang Ingin di Rubah : ')
                    listMurid[4]['alamat'] = alamat_5
                    daftarMurid()
                elif Data5 == 4 :
                    print('Daftar Murid\n')
                    print('Nama | ID| Alamat| Nilai')
                    print(listMurid[4]['nama'],listMurid[4]['ID'],listMurid[4]['alamat'],listMurid[4]['Nilai'])
                    Nilai_5 = int(input('Silahkan Masukan Nilai Yang Ingin di Rubah : '))
                    listMurid[4]['Nilai'] = Nilai_5
                    daftarMurid()
                else :
                    print(menuEdit)               
        else:
            break

while True :
    Input_menu = int(input('''
        Selamat Datang Menu Admin Purwadhika

        List Menu :
        1. Menampilkan Daftar Murid
        2. Edit Data
        3. Exit Program

        Masukkan angka Menu yang ingin dijalankan : '''))
       
    if (Input_menu == 1) :
        daftarMurid()
    elif (Input_menu == 2) :
        edit_menu()
    elif (Input_menu == 3) :
        print('Sampai Jumpah')
        break

                    


            

               
                



            


