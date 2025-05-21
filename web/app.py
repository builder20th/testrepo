from flask import Flask, render_template_string
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('POSTGRES_USER', 'postgres'),
        password=os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        dbname=os.environ.get('POSTGRES_DB', 'weather')
    )
    return conn

@app.route('/')
def index():
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
