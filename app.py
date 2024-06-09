from flask import Flask, render_template, request, jsonify
from property import propertyPredict
from land import landPredict
from daerah import daerah

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        aset = request.form.get('tipe')
        if aset == "land":
            luas_tanah = request.form.get('luas_tanah', '0')
            kecamatan = request.form.get('kecamatan', '')
            predict = landPredict(
                luas_tanah, kecamatan
            )
            interpretation = f"Considering the vast expanse of land spanning {luas_tanah} square meters, nestled in the serene locale of {kecamatan}, this prediction takes into account various factors to determine its estimated value. The fertile grounds of this plot, coupled with its strategic location in {kecamatan}, contribute to its potential value. With meticulous analysis and data-driven insights, the predicted price reflects not just the raw land area, but also the promising prospects it holds for development or investment. It's a canvas of opportunity waiting to be explored, promising returns and prosperity in the realm of real estate."
            return render_template('index.html', prediction=predict, daerah=daerah, interpretation=interpretation)
        else:
            luas_bangunan = float(request.form.get('luas_bangunan', '0'))
            luas_tanah = float(request.form.get('luas_tanah', '0'))
            tipe = request.form.get('tipe', '')
            kamar_tidur = int(request.form.get('kamar_tidur', '0'))
            kamar_mandi = int(request.form.get('kamar_mandi', '0'))
            lantai = int(request.form.get('lantai', '0'))
            kecamatan = request.form.get('kecamatan', '')

            # Assuming propertyPredict is a function that returns the prediction
            predict = propertyPredict(
                luas_bangunan, luas_tanah, tipe, kamar_tidur, kamar_mandi, lantai, kecamatan)

            interpretation = f"Delving into the essence of this property's allure, we unravel a narrative of bespoke elegance and modern living. With an expansive building area spanning {luas_bangunan} square meters and a sprawling land area of {luas_tanah} square meters, this property embodies a harmonious blend of space and sophistication. Its {tipe} architectural style, accentuated by {kamar_tidur} bedrooms and {kamar_mandi} bathrooms, creates an ambiance of comfort and luxury. Ascending through {lantai} floor(s) reveals panoramic vistas, offering a glimpse into a lifestyle of opulence. Nestled within the vibrant {kecamatan} district, this property epitomizes convenience and connectivity. Through meticulous analysis and advanced algorithms, the predicted price encapsulates not just the tangible aspects but also the intangible essence of this remarkable abode, reflecting its true value in today's dynamic real estate landscape."
            return render_template('index.html', prediction=predict, daerah=daerah, interpretation=interpretation)

    elif request.method == 'GET':
        prediction = request.args.get('predict')
        if prediction == 'Land':
            return render_template('index.html', prediction=None, status="land", daerah=daerah)
            # return "test1"
        elif prediction == 'Properties':
            return render_template('index.html', prediction=None, status="properties", daerah=daerah)
            # return "test2"
        else:
            # Handle the case when neither 'Land' nor 'Properties' are in request args
            return render_template('index.html', prediction=None, status='land', daerah=daerah)
            # return "test3"

    else:
        # Handle other cases where request.method is neither 'GET' nor 'POST'
        return render_template('index.html', prediction=None, status='land', daerah=daerah)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
