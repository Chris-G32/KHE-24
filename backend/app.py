from scam_detection.job_analysis import Job
from scam_detection.analyzer import Analyzer
from db.db import *

from flask import Flask, jsonify, request

app = Flask(__name__)

analyzer = Analyzer()

@app.route("/report", methods=['POST'])
def report_route():
    request_data = request.get_json()

    contact = ContactInfo(phone_number=request_data["phone"], email=request_data["email"], name=request_data["name"])
    job = Job(request_data["domain"], request_data["link"], request_data["position_title"], request_data["description"], request_data["company"], contact)

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