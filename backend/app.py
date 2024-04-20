import sys 
import os
from scam_detection.text_analysis import analyze_spelling

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/detect", methods=['POST'])
def detect_route():
    request_data = request.get_json()

    result = analyze_spelling(request_data["body"])

    response = {
        "errors": result[0],
        "total": result[1]
    }

    return jsonify(response)

@app.route("/report", methods=['POST'])
def report():
    request_data = request.get_json()

    response = {}

    return jsonify(response)