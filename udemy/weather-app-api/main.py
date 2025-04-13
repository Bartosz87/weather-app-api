from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


stations = pd.read_csv("stations_data/stations.txt", skiprows=17)
stations['STANAME0'] = stations["STANAME                                 "].str.strip()
stations_list = stations['STANAME0']

@app.route("/")
def home():
    return render_template("home.html", stations_list= stations_list)


@app.route('/submit', methods=['POST'])
def submit():
    date = request.form['weather-date']
    station = request.form['station']

    #na podstawie nazwy miasta znajduję jego id
    citi_id = stations[stations['STANAME0'] == "LINKOEPING"]['STAID'].iloc[0]

    #uzupełniam id o brakujące zera zgodnie z formatem stacji
    citi_id=str(citi_id).rjust(6, "0")
    station_name = f"TG_STAID{citi_id}.txt"

    #wczytuję plik z danymi dla podanej stacji
    df = pd.read_csv(f"stations_data/{station_name}", skiprows=20, parse_dates=["    DATE"])
    df["TG0"] = df["   TG"].mask(df["   TG"] == -9999)
    df["TG0"] = df["TG0"] / 10
    df.columns = df.columns.str.strip()

    #sprawdzam czy data mieści się w zakresie pomiarowym i podaję odczyt
    if date in df["DATE"].values:
        temp_readout = str(df[df["DATE"] == date]["TG0"].iloc[0])
    else:
        temperature ="No read out"

    return{
        "station":station,
        "date": date,
        "remperature": temperature
    }



if __name__ == "__main__":
    app.run(debug=True, port=5001)