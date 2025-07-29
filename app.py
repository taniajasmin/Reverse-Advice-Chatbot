# from flask import Flask, render_template, request
# from advice_engine import get_bad_advice

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     advice = None
#     question = None
#     if request.method == 'POST':
#         question = request.form.get('question')
#         if question:
#             advice = get_bad_advice(question)
#     return render_template('index.html', question=question, advice=advice)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, session
from advice_engine import get_bad_advice
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure key in production

# Initialize session history if not present
@app.before_request
def initialize_history():
    if 'history' not in session:
        session['history'] = []

@app.route('/', methods=['GET', 'POST'])
def index():
    history = session.get('history', [])
    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            advice = get_bad_advice(question)
            history.append((question, advice))
            session['history'] = history
    return render_template('index.html', history=history)

if __name__ == '__main__':
    app.run(debug=True)