import psycopg2
import sys
sys.path.append('models')
sys.path.append('scam_detection')

from models import User, Feedback
from job_analysis import AnalysisResults, Job, ContactInfo

import phonenumbers

conn = psycopg2.connect(database = "khe2024", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "12345",
                        port = 5432)

def create_user(email, first_name, last_name) -> int:
    cur = conn.cursor()
    sql_query = "INSERT INTO \"user\" (email, first_name, last_name) VALUES (%s, %s, %s) RETURNING user_id;"
    cur.execute(sql_query, (email, first_name, last_name))
    conn.commit()
    id = cur.fetchone()[0]
    cur.close()
    return id

def create_job(job:Job) -> int:
    cur = conn.cursor()
    sql_query = "INSERT INTO \"job\" (link, domain, position, description, contact_name, contact_phone, contact_email, company, post_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING job_id;"
    cur.execute(sql_query, (job.link, job.domain, job.position_title, job.description, job.contact_info.name, phonenumbers.format_in_original_format(job.contact_info.phone_number, "US"), job.contact_info.email, job.company, job.post_date))
    conn.commit()
    id = cur.fetchone()[0]
    cur.close()
    return id

def create_report(report:AnalysisResults, job_id:int) -> int:
    cur = conn.cursor()
    sql_query = "INSERT INTO \"report\" (job_id, summary, spelling_errors, grammar_errors, suspicious_email, suspicious_phone, suspicious_link, ai_risk, cumulative_risk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING report_id;"
    cur.execute(sql_query, (job_id, report.ai_summary, report.spelling_error_count, report.grammar_error_count, report.email_suspicious, report.phone_suspicious, report.link_suspicious, report.ai_analysis, report.cumulative_risk))
    conn.commit()
    id = cur.fetchone()[0]
    cur.close()
    return id

def create_feedback(feedback:Feedback):
    cur = conn.cursor()
    sql_query = "INSERT INTO feedback (email, report_id, feedback) VALUES (%s, %s, %s);"
    cur.execute(sql_query, (feedback.email, feedback.report_id, feedback.feedback))
    conn.commit()
    cur.close()
    pass

def create_bookmark(user_id, report_id):
    cur = conn.cursor()
    sql_query = "INSERT INTO bookmarks (user_id, report_id) VALUES (%s, %s)"
    cur.execute(sql_query, (user_id, report_id))
    cur.close()
    pass

def get_report_by_id(id:int):
    cur = conn.cursor()
    sql_query = "SELECT job_id, summary, spelling_errors, grammar_errors, suspicious_email, suspicious_phone, suspicious_link, ai_risk, cumulative_risk FROM report WHERE report_id=%s"
    cur.execute(sql_query, (id, ))
    res = cur.fetchone()
    report_result = AnalysisResults()
    report_result.spelling_error_count=res[2]
    report_result.grammar_error_count=res[3]
    report_result.email_suspicious=res[4]
    report_result.link_suspicious=res[6]
    report_result.phone_suspicious=res[5]
    report_result.ai_analysis=res[7]
    report_result.ai_summary=res[1]
    report_result.cumulative_risk=res[8]
    job_id = res[0]
    return (report_result, job_id)

def get_job_by_id(id:int):
    cur = conn.cursor()
    sql_query = "SELECT link, domain, position, description, contact_name, contact_phone, contact_email, company, post_date FROM job WHERE job_id=%s"
    cur.execute(sql_query, (id, ))
    res = cur.fetchone()
    contact_result = ContactInfo(phone_number=res[5], email=res[6], name=res[4])
    job_result = Job(domain=res[1], link=res[0], position_title=res[2], description=res[3], company=res[7], post_date=res[8], contact_info=contact_result)
    return job_result


def get_bookmarks_by_user(user_id):
    cur = conn.cursor()
    sql_query = "SELECT * FROM bookmarks JOIN report ON bookmarks.report_id=report.report_id WHERE user_id=%s"
    cur.execute(sql_query, (user_id, ))
    res = cur.fetchall()
    return res

def get_user_by_email(email) -> User:
    cur = conn.cursor()
    sql_query = 'SELECT * FROM "user" WHERE email=%s'
    cur.execute(sql_query, (email,))
    res = cur.fetchone()
    user = User(user_id=res[0], email=res[1], first_name=res[6], last_name=res[7])
    cur.close()
    return user

def get_feedback_by_report(report_id):
    cur = conn.cursor()
    sql_query = "SELECT email, feedback FROM feedback WHERE report_id=%s"
    cur.execute(sql_query, (report_id, ))
    res = cur.fetchall()
    feedback_list = []
    for element in res:
        feedback_list.append({
            'email': element[0],
            'report_id': report_id,
            'feedback': element[1]})
    
    return feedback_list

if __name__ == '__main__':
    test_user = User('test2@gmail.com', 'test2', 'tester2')
    # create_user(test_user)
    # print(get_user_by_email('test2@gmail.com').first_name)
    test_contact = ContactInfo('330-217-0155', 'test@test.test', 'Bailey')
    test_job = Job('linkedin.com', 'http://myworkday.com/bullshit', 'BS Cleaner', 'This position requires you to deal with Aziz Jadaine', test_contact)
    # print(create_job(test_job))
    test_report = AnalysisResults()
    test_report.spelling_error_count=10
    test_report.grammar_error_count=5
    test_report.email_suspicious=False
    test_report.link_suspicious=True
    test_report.phone_suspicious=False
    test_report.ai_analysis="Medium"
    test_report.ai_summary="This is a job."
    test_report.cumulative_risk="High"
    # create_report(test_report, 1)
    print(get_report_by_id(1).spelling_error_count)
