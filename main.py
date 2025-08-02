# main.py

from flask import Flask

app = Flask(__app__)  # Yeh 'app' object Gunicorn ko chahiye hota hai

@app.route("/")
def home():
    return "Hello from Flask in main.py!"
