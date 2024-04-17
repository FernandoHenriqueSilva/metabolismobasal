# app.py -
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    gender = request.form['gender']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age'])

    if gender == 'male':
        basal_metabolism = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        basal_metabolism = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return render_template('result.html', basal_metabolism=basal_metabolism)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)
