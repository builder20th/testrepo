from flask import Flask, render_template_string
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
    update_weather_data()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT country, temperature, humidity FROM weather')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    html = '<h1>Weather Data</h1><table border="1"><tr><th>Country</th><th>Temperature (C)</th><th>Humidity (%)</th></tr>'
    for country, temp, humidity in rows:
        html += f'<tr><td>{country}</td><td>{temp}</td><td>{humidity}</td></tr>'
    html += '</table>'
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
