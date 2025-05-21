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
    html = '''
    <!doctype html>
    <html>
    <head>
        <title>Weather Data</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            table { border-collapse: collapse; width: 60%; margin: auto; }
            th, td { padding: 8px 12px; border: 1px solid #ccc; text-align: center; }
            th { background-color: #f4f4f4; }
            h1 { text-align: center; }
        </style>
    </head>
    <body>
        <h1>Weather Data</h1>
        <table>
            <tr><th>Country</th><th>Temperature (C)</th><th>Humidity (%)</th></tr>
    '''
    for country, temp, humidity in rows:
        html += f'<tr><td>{country}</td><td>{temp}</td><td>{humidity}</td></tr>'
    html += '''
        </table>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
