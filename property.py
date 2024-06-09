import joblib
import numpy as np
# import sklearn

# Memuat model yang sudah dilatih
model = joblib.load("property_model.joblib")

def propertyPredict(luas_bangunan, luas_tanah, tipe, kamar_tidur, kamar_mandi, lantai, kecamatan):
    # Inisialisasi array input dengan semua nilai 0
    input_data = np.zeros(154) 

    # Mengisi nilai numerik
    input_data[0] = luas_bangunan
    input_data[1] = luas_tanah
    # Handling division by zero with numpy, more appropriate for numeric computations
    input_data[2] = luas_bangunan / luas_tanah if luas_tanah != 0 else 0

    # Mengisi nilai kategori 'Tipe'
    if tipe == 'Rumah':
        input_data[3] = 1
    elif tipe == 'Villa':
        input_data[4] = 1

    # Mengisi nilai one-hot encoding untuk 'Kamar tidur'
    kamar_tidur_dict = {10: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, '>10': 14}
    if kamar_tidur in kamar_tidur_dict:
        input_data[kamar_tidur_dict[kamar_tidur]] = 1

    # Mengisi nilai one-hot encoding untuk 'Kamar Mandi'
    kamar_mandi_dict = {10: 15, 2: 16, 3: 17, 4: 18, 5: 19, 6: 20, 7: 21, 8: 22, 9: 23, '>10': 24}
    if kamar_mandi in kamar_mandi_dict:
        input_data[kamar_mandi_dict[kamar_mandi]] = 1

    # Mengisi nilai one-hot encoding untuk 'Lantai'
    lantai_dict = {2: 25, 3: 26, 4: 27}
    if lantai in lantai_dict:
        input_data[lantai_dict[lantai]] = 1

    kecamatan_index = 28
    kecamatan_dict = {kec: index for index, kec in enumerate([
        "Abianbase", "Abiansemal", "Angantaka", "Antapan", "Bajera", "Balangan", "Baluk", "Bangli",
        "Banjar", "Banjaranyar", "Batannyuh", "Batu Belig", "Batuan", "Baturiti", "Bebalang", "Benoa",
        "Beringkit", "Bitera", "Bongan", "Bukit", "Buleleng", "Canggu", "Cemagi", "Cepaka", "Dalung",
        "Dalung Permai", "Danginpuri Kaja", "Danginpuri Kangin", "Danginpuri Kelod", "Dauhpuri Kelod", "Dawan",
        "Dencarik", "Denpasar Barat", "Denpasar Selatan", "Denpasar Timur", "Denpasar Utara", "Gatot Subroto",
        "Gelogor Carik", "Gianyar", "Gubug", "Gunung Salak", "Jimbaran", "Kalibubuk", "Kapal", "Karang Asem",
        "Kediri", "Kedonganan", "Kemenuh", "Kerambitan", "Kerobokan", "Kerobokan Kaja", "Kerobokan Kelod", "Kesiman",
        "Klungkung", "Klungkung Kota", "Kubutambahan", "Kuta", "Kuta Selatan", "Kuta Utara", "Kutuh", "Lelateng",
        "Lovina", "Lukluk", "Mahendradata", "Marga", "Medahan", "Mengwi", "Mumbul", "Munggu", "Nusa Dua", 
        "Padangsambian Kaja", "Padangsambian Kelod", "Pancasari", "Pangkungkarung", "Pangkutibah", "Panjer", "Pecatu",
        "Pedungan", "Peguyangan", "Peguyangan Kaja", "Peguyangan Kangin", "Pejeng", "Pejeng Kaja", "Pemecutan",
        "Pemecutan Kaja", "Pemecutan Kelod", "Pemogan", "Pemuteran", "Penarungan", "Penatih", "Penatihdanginpuri",
        "Perancak", "Pererenan", "Pesanggaran", "Petang", "Puri Gading", "Renon", "Salemadeg Timur", "Sambangan",
        "Sangsit", "Sanur", "Sanur Kaja", "Semarapura Kangin", "Semer", "Seminyak", "Seririt", "Sesetan",
        "Siangan", "Sibang Gede", "Sidakarya", "Subagan", "Sukasada", "Sukawati", "Sunset Road", "Tabanan", "Taman Griya",
        "Tampak Siring", "Tegallalang", "Tonja", "Tulamben", "Tumbu", "Ubud", "Ubung Kaja", "Uluwatu", "Umalas", "Ungasan"
    ], start=kecamatan_index)}

    if kecamatan in kecamatan_dict:
        input_data[kecamatan_dict[kecamatan]] = 1   

    # Melakukan prediksi
    prediksi = model.predict([input_data])
    prediksi_asli = np.exp(prediksi) # Gua gapaham ini gimana yang bener
    predict = "Rp. {:,.0f}".format(float(prediksi_asli)).replace(".", ",")

    return predict