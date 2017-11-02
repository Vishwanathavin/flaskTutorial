from flask import Flask, url_for,render_template
app = Flask(__name__)



@app.route('/index/')
def index():
    href = "{{ url_for('static', filename='style.css')}}"
    # url_for('static', filename='style.css')
    return render_template('./index.html')