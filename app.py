from flask import Flask, request, jsonify
import time;

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"
