from flask import Flask, render_template, request, jsonify
from property import propertyPredict
from land import landPredict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # prediction = request.args.get('prediction', 'ini kalo isi')
    # prediction = request.args.get('prediction')
    # return render_template('index.html', prediction=prediction)
    if request.method == 'POST':
        # tipe = request.form.get('tipe', '')
        # if tipe == 'Property':
        luas_bangunan = float(request.form.get('luas_bangunan', '0'))
        luas_tanah = float(request.form.get('luas_tanah', '0'))
        tipe = request.form.get('tipe', '')
        kamar_tidur = int(request.form.get('kamar_tidur', '0'))
        kamar_mandi = int(request.form.get('kamar_mandi', '0'))
        lantai = int(request.form.get('lantai', '0'))
        kecamatan = request.form.get('kecamatan', '')
        # Call the prediction function
        predict = propertyPredict(luas_bangunan, luas_tanah, tipe, kamar_tidur, kamar_mandi, lantai, kecamatan)
            
        # elif tipe == 'Land':
        # luas_tanah = float(request.form.get('luas_tanah', '0'))
        # kecamatan = request.form.get('kecamatan', '')

        # predict = landPredict(luas_tanah, kecamatan)

        return render_template('index.html', prediction=predict)
    
    return render_template('index.html', prediction=None)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
