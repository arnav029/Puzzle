from flask import Flask, jsonify, send_from_directory, request
import json
import datetime
import os

app = Flask(__name__)

with open('reflections.json', 'r', encoding='utf-8') as f:
    REFLECTIONS_DATA = json.load(f)

def get_ist_time():
    """Calculates current datetime in IST (UTC+5:30)"""
    utc_now = datetime.datetime.utcnow()
    return utc_now + datetime.timedelta(hours=5, minutes=30)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/api/today')
def get_daily_reflection():
    today_str = get_ist_time().strftime("%d/%m/%Y")
    daily_entry = next((item for item in REFLECTIONS_DATA if item["date"] == today_str), None)
    
    if daily_entry:
        return jsonify(daily_entry)
    else:
        return jsonify({"reflection": "Silence for today.", "perspective": "No record found."})

@app.route('/api/archive')
def get_archive():
    requested_date_str = request.args.get('date')
    
    if not requested_date_str:
        return jsonify({"error": "No date provided"}), 400

    try:
        req_date = datetime.datetime.strptime(requested_date_str, "%d/%m/%Y").date()
        current_ist_date = get_ist_time().date()
        
        if req_date >= current_ist_date:
            return jsonify({"error": "You cannot look into the future."}), 403
            
        entry = next((item for item in REFLECTIONS_DATA if item["date"] == requested_date_str), None)
        return jsonify(entry if entry else {"error": "Date not found"})
        
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)