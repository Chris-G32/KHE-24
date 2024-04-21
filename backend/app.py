from scam_detection.job_analysis import Job, ContactInfo
from scam_detection.analyzer import Analyzer
from db.db import *

from flask import Flask, jsonify, request

app = Flask(__name__)

analyzer = Analyzer()

@app.route("/report", methods=['POST', 'GET'])
def report_route():
    if request.method == 'POST':
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
    else:
        id = request.args.get('report_id')

        report = get_report_by_id(id)

        results = {
            "result": {
                "spelling_error_count": report.spelling_error_count,
                "grammar_error_count": report.grammar_error_count,
                "email_suspicious": report.email_suspicious,
                "link_suspicious": report.link_suspicious,
                "phone_suspicious": report.phone_suspicious,
                "pay_suspicious": report.pay_suspicious,
                "ai_analysis": report.ai_analysis,
                "ai_summary": report.ai_summary,
                "ai_skills": report.ai_skills,
                "cumulative_risk": report.cumulative_risk
            }
        }

        return jsonify(results)


@app.route("/bookmark", methods=['POST', 'GET'])
def bookmark():
    if request.method == 'POST':
        request_data = request.get_json()

        create_bookmark(request_data["user_id"], request_data["report_id"])

        return jsonify()
    else:
        user_id = request.args.get('user_id')

        res = get_bookmarks_by_user(user_id)

        return res
    
@app.route("/user", methods=['POST'])
def user():
    request_data = request.get_json()

    id = create_user(
        request_data["email"],
        request_data["first_name"],
        request_data["last_name"]
        )

    return jsonify({"id": id})