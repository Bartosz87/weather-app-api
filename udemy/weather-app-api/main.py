from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/vi/<station>/<date>")
def station(station, date):
    temperature = 11
    return{
        "station":station,
        "date": date,
        "remperature": temperature

    }

@app.route('/submit', methods=['POST'])
def submit():
    date = request.form['weather-date']

    temperature = 11
    station = "warszawa-bródno"
    return{
        "station":station,
        "date": date,
        "remperature": temperature
    }



if __name__ == "__main__":
    app.run(debug=True, port=5001)