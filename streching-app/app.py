from flask import Flask, render_template, request
from stretches_data import STRETCHES

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stretches/<posture>')
def show_stretches(posture):
    stretches = STRETCHES.get(posture, [])
    return render_template('stretches.html', posture=posture, stretches=stretches)

if __name__ == '__main__':
    app.run(debug=True)
