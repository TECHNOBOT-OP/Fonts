from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def majn():
    man = url_for('static', filename='font.css')
    return man
