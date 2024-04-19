from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# List to store exam dates
exam_dates = []

@app.route('/')
def index():
    return render_template('exm.html', exam_dates=exam_dates)

@app.route('/add_exam', methods=['POST'])
def add_exam():
    exam_date_str = request.form['exam_date']
    exam_name = request.form['exam_name']

    # Convert the input string to a datetime object
    exam_date = datetime.strptime(exam_date_str, '%Y-%m-%d').date()

    # Calculate the number of days until the exam
    days_until_exam = (exam_date - datetime.now().date()).days

    exam_info = {'name': exam_name, 'date': exam_date_str, 'days_until_exam': days_until_exam}
    exam_dates.append(exam_info)

    return render_template('exm.html', exam_dates=exam_dates)

if __name__ == '__main__':
    app.run(debug=True)

