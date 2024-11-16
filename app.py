from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Data dummy untuk kelas
data_kelas = [
    {"nama": "Ali", "kelas": "10A", "nilai": 90},
    {"nama": "Budi", "kelas": "10B", "nilai": 85},
    {"nama": "Citra", "kelas": "10A", "nilai": 88},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(data_kelas)

if __name__ == '__main__':
    app.run(debug=True)
