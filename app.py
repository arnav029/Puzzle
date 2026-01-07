from flask import Flask, jsonify, send_from_directory
import json
import datetime
import os

app = Flask(__name__)

# --- LOAD DATA SECURELY ON SERVER START ---
# We load the data into memory. The file 'reflections.json' 
# is NEVER exposed to the public internet directly.
with open('reflections.json', 'r', encoding='utf-8') as f:
    REFLECTIONS_DATA = json.load(f)

def get_ist_date_str():
    """Calculates current date in IST (UTC+5:30)"""
    utc_now = datetime.datetime.utcnow()
    ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)
    return ist_now.strftime("%d/%m/%Y")

@app.route('/')
def home():
    """Serves the frontend"""
    return send_from_directory('.', 'index.html')

@app.route('/api/today')
def get_daily_reflection():
    """
    API Endpoint: Returns ONLY today's reflection.
    The browser hits this instead of downloading the whole JSON.
    """
    today_str = get_ist_date_str()
    
    # Find the matching entry
    daily_entry = next((item for item in REFLECTIONS_DATA if item["date"] == today_str), None)
    
    if daily_entry:
        return jsonify(daily_entry)
    else:
        return jsonify({
            "reflection": "Silence for today.", 
            "perspective": "No record found."
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)