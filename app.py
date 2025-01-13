from flask import Flask,jsonify, request, render_template  
from flask_cors import CORS

import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/count_exercise', methods=['POST'])
def count_exercise():
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400
    
    exercise = data.get('exercise')
    if exercise is None:
        return jsonify({'error': 'Exercise parameter not found in JSON data'}), 400
    
    if exercise == 'reps':
        count = subprocess.check_output(['python', 'Reps.py']).decode().strip()
    elif exercise == 'squats':
        count = subprocess.check_output(['python', 'Squats.py']).decode().strip()
    elif exercise == 'pushups':
        count = subprocess.check_output(['python', 'Pushups.py']).decode().strip()
    else:
        count = 'Error: Invalid exercise'
    return jsonify({'count': count})

if __name__ == '__main__':
    app.run(debug=True)
