from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

RESULTS_FILE = "results.csv"

if not os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["block", "trial", "actual_color", "response"])

@app.route('/')
def home():
    return "Сервер працює!"

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.json  

    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400

    with open(RESULTS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([data["block"], data["trial"], data["actual_color"], data["response"]])

    return jsonify({"status": "success", "message": "Data saved successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
