import joblib
import numpy as np
# import sklearn

# Memuat model yang sudah dilatih
model = joblib.load("land_model.joblib")

def landPredict(luas_tanah, kecamatan):
    # Inisialisasi array input dengan semua nilai 0
    input_data = np.zeros(154) 

    input_data[0] = luas_tanah

    kecamatan_index = 1
    kecamatan_dict = {kec: index for index, kec in enumerate([
        "Abuan", "Airkuning", "Amed", "Angseri", "Antap", "Antosari", "Anturan", "Babahan",
        "Baktiseraga", "Balangan", "Banjar", "Banjarankan", "Bantas", "Batu Belig",
        "Batur Selatan", "Batur Tengah", "Baturiti", "Bebandem", "Bedugul",
        "Belah Batuh (Blahbatuh)", "Belalang", "Belimbing", "Bengkala", "Benoa", "Beraban",
        "Besakih", "Blahbatuh", "Bukian", "Buleleng", "Bulian", "Candi Dasa", "Candikesuma",
        "Canggu", "Celukanbawang", "Cemagi", "Cempaga", "Dalang", "Dalung", "Dalung Permai",
        "Danginpuri", "Dauhpuri", "Dauhpuri Kauh", "Dencarik", "Denpasar Barat",
        "Denpasar Selatan", "Denpasar Timur", "Denpasar Utara", "Depeha", "Dewi Sri",
        "Gadungan", "Gelgel", "Gerokgak", "Gesing", "Gianyar", "Goa Gong", "Jimbaran",
        "Kaba kaba", "Kaliasem", "Karang Asem", "Kartika Plaza", "Kayuputih", "Kediri",
        "Kelating", "Keramas", "Kerambitan", "Kerobokan", "Kerta", "Kesiman", "Kintamani",
        "Kubutambahan", "Kuta", "Kuta Selatan", "Kuta Utara", "Lalanglinggah", "Lovina",
        "Mahendradata", "Mambang", "Megati", "Mendoyo", "Mengwi", "Menyali", "Munduk",
        "Munggu", "Negara", "Ngurah Rai", "Nusa Dua", "Nusa Penida", "Nusapenida", "Nyanyi",
        "Pandakgede", "Pangkungparuk", "Panjer", "Panji", "Payangan", "Pecatu", "Peguyangan",
        "Pejeng Kangin", "Pejeng Kelod", "Pekutatan", "Pemaron", "Pemuteran", "Penarungan",
        "Penebel", "Penuktukan", "Pererenan", "Petang", "Petitenget", "Pupuan", "Pupuansawah",
        "Renon", "Saba", "Sading", "Salemadeg Barat", "Salemadeg Timur", "Sanda", "Sanding",
        "Sanur", "Sawan", "Selemadeg", "Sembung", "Seminyak", "Sempidi", "Serangan", "Seraya",
        "Sidemen", "Singaraja", "Sudaji", "Sukasada", "Sukawati", "Sumberkimia", "Sunset Road",
        "Susut", "Tabanan", "Tajun", "Taman Griya", "Tanah Lot", "Tangguntiti", "Tegallalang",
        "Tegalmengkeb", "Tejakula", "Tembok", "Tibubeneng", "Tigawasa", "Tinga tinga", "Tuban",
        "Tulikup", "Tunjung", "Ubud", "Ubung", "Ubung Kaja", "Umalas", "Ungasan", "Wanasari"
    ], start=kecamatan_index)}

    if kecamatan in kecamatan_dict:
        input_data[kecamatan_dict[kecamatan]] = 1   

    # Melakukan prediksi
    prediksi = model.predict([input_data])
    prediksi_asli = np.exp(prediksi) # Gua gapaham ini gimana yang bener
    predict = "Rp. {:,.0f}".format(float(prediksi_asli)).replace(".", ",")

    return predict
