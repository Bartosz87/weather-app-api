from flask import Flask, render_template, request, jsonify
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
    start_date_form = request.form['weather-date']
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

    start_date = pd.to_datetime(start_date_form)


    #sprawdzam czy data mieści się w zakresie pomiarowym i podaję odczyt
    if start_date in df["DATE"].values:
        filtered_df = df[(df['DATE'] >= start_date)][:60]
    else:
        return render_template("home.html", stations_list=stations_list, comment="Date out of scope. Chose different one.")

    filtered_df['DATE'] = filtered_df['DATE'].astype(str)

    date_set = filtered_df['DATE'].tolist()
    temp_set = filtered_df["TG0"].tolist()

    return render_template("station-data.html",  date_set=date_set, temp_set=temp_set,
        station_default=station, start_date=start_date, start_date_form=start_date_form, stations_list= stations_list )


if __name__ == "__main__":
    app.run(debug=True, port=5001)

