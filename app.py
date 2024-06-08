from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    # prediction = request.args.get('prediction', 'ini kalo isi')
    prediction = request.args.get('prediction')
    return render_template('index.html', prediction=prediction)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
