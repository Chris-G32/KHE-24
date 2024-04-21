import sys 
import os
from scam_detection.text_analysis import analyze_spelling
from scam_detection.job_analysis import Job
from scam_detection.analyzer import Analyzer
from db.db import *

from flask import Flask, jsonify, request

app = Flask(__name__)

analyzer = Analyzer()

@app.route("/report", methods=['POST'])
def report_route():
    request_data = request.get_json()

    job = Job(request_data["domain"], request_data["link"])

    res = analyzer.run_analysis(job)

    job_id = create_job(job)
    create_report(res, job_id)

    results = {
        "job": job,
        "report": res
    }

    return jsonify(results)


@app.route("/report", methods=['POST'])
def report():
    request_data = request.get_json()

    response = {}

    return jsonify(response)