from openai import OpenAI

client = OpenAI()

def generate_GPT(job_description):
    # Summary generation
    summary_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize this Job Description '{}' Focus more on the job itself rather than the hiring company. The length of the summary should be between 100 and 150 words. Make it as concise as possible but make sure to keep it highly informative.".format(job_description)},
        ]
    )
    summary = summary_completion.choices[0].message.content

    # Risk generation
    risk_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "You can only use ONE WORD to reply to this prompt: Very low, Low, Medium, and High. What is the risk of this job description '{}' being a Scam ?".format(job_description)},
        ]
    )
    risk = risk_completion.choices[0].message.content

    return summary, risk