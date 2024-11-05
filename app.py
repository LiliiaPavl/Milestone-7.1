import csv
from flask import Flask, jsonify

app = Flask(__name__)

def load_data():
    with open('database.csv', mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    data = load_data()

    response = {
        "total": len(data),
        "employees": data
    }
    
    return jsonify(response)

@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    data = load_data()

    response = {
        "total": len(data),
        "employees": data
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
