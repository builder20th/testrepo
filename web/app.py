from flask import Flask, render_template_string, request
import os
import psycopg2
import random

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('POSTGRES_USER', 'postgres'),
        password=os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        dbname=os.environ.get('POSTGRES_DB', 'weather')
    )
    return conn

def update_weather_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT country FROM weather')
    countries = [row[0] for row in cur.fetchall()]
    for country in countries:
        temp = random.randint(15, 35)
        humidity = random.randint(40, 80)
        cur.execute(
            'UPDATE weather SET temperature = %s, humidity = %s WHERE country = %s',
            (temp, humidity, country)
        )
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():

    country = request.args.get('country')

    conn = get_db_connection()
    cur = conn.cursor()
    if country:
        cur.execute(
            'SELECT country, temperature, humidity FROM weather WHERE country ILIKE %s',
            (country,)
        )
    else:
        cur.execute('SELECT country, temperature, humidity FROM weather')
    rows = cur.fetchall()
    cur.close()
    conn.close()

    html = '''<style>
        body { background: linear-gradient(to bottom, #ffffff, #e0f0ff); font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 8px; text-align: left; }
        th { background: #4CAF50; color: white; }
        tr:nth-child(even) { background: #f2f2f2; }
        .flag { width: 40px; height: 25px; border: 1px solid #000; }
        .flag-de { background: linear-gradient(to bottom, black 0%, black 33%, red 33%, red 66%, gold 66%, gold 100%); }
        .flag-us { background: repeating-linear-gradient(to bottom, red 0, red 10%, white 10%, white 20%); }
        .flag-es { background: linear-gradient(to bottom, red 0%, red 25%, #ffc400 25%, #ffc400 75%, red 75%, red 100%); }
        .flag-fr { background: linear-gradient(to right, blue 0%, blue 33%, white 33%, white 66%, red 66%, red 100%); }
        .flag-it { background: linear-gradient(to right, green 0%, green 33%, white 33%, white 66%, red 66%, red 100%); }
        .flag-ca { background: linear-gradient(to right, red 0%, red 25%, white 25%, white 75%, red 75%, red 100%); }
        .flag-br { background: green; position: relative; }
        .flag-br::after { content: ''; position: absolute; top: 4px; left: 8px; width: 24px; height: 16px; background: yellow; transform: rotate(45deg); }
        .flag-jp { background: white; position: relative; }
        .flag-jp::after { content: ''; position: absolute; top: 5px; left: 13px; width: 14px; height: 14px; background: red; border-radius: 50%; }
    </style>'''
    html += '<h1>Weather Data</h1>'
    html += '<form method="get">'
    html += '<input type="text" name="country" placeholder="Country"'
    if country:
        html += f' value="{country}"'
    html += '>'
    html += '<input type="submit" value="Search">'
    html += '</form>'
    flag_map = {
        'Deutschland': 'de',
        'USA': 'us',
        'Spanien': 'es',
        'Frankreich': 'fr',
        'Italien': 'it',
        'Kanada': 'ca',
        'Brasilien': 'br',
        'Japan': 'jp'
    }
    html += '<table border="1"><tr><th>Flag</th><th>Country</th><th>Temperature (C)</th><th>Humidity (%)</th></tr>'
    for c, temp, humidity in rows:
        cls = flag_map.get(c, '')
        flag_div = f'<div class="flag flag-{cls}"></div>' if cls else ''
        html += f'<tr><td>{flag_div}</td><td>{c}</td><td>{temp}</td><td>{humidity}</td></tr>'
    html += '</table>'

    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
