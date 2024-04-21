from scam_detection.job_analysis import Job, ContactInfo
from scam_detection.analyzer import Analyzer
from db.db import *

from flask import Flask, jsonify, request

app = Flask(__name__)

analyzer = Analyzer()

@app.route("/report", methods=['POST'])
def report_route():
    request_data = request.get_json()

    contact = ContactInfo(phone_number=request_data["phone_number"], email=request_data["email"], name=request_data["name"])

    job = Job(request_data["domain"], request_data["link"], request_data["position_title"], request_data["description"], request_data["company"], request_data["post_date"], contact_info=contact)

    job.display()

    res = analyzer.run_analysis(job)

    job_id = create_job(job)
    create_report(res, job_id)

    results = {
        "job": {
            "job_id": job_id,
            "domain": job.domain,
            "link": job.link,
            "position_title": job.position_title,
            "description": job.description,
            "company": job.company,
            "contact": {
                "phone_number": request_data["phone_number"],
                "email": job.contact_info.email,
                "name": job.contact_info.name
            }
        },
        "result": {
            "spelling_error_count": res.spelling_error_count,
            "grammar_error_count": res.grammar_error_count,
            "email_suspicious": res.email_suspicious,
            "link_suspicious": res.link_suspicious,
            "phone_suspicious": res.phone_suspicious,
            "pay_suspicious": res.pay_suspicious,
            "ai_analysis": res.ai_analysis,
            "ai_summary": res.ai_summary,
            "ai_skills": res.ai_skills,
            "cumulative_risk": res.cumulative_risk
        }
    }

    return jsonify(results)