BEGIN;

CREATE TABLE IF NOT EXISTS public.user
(
    user_id INTEGER GENERATED ALWAYS AS IDENTITY,
    email CHARACTER VARYING(255) UNIQUE NOT NULL,
    industry CHARACTER VARYING(50),
    years_of_experience INTEGER,
    salary INTEGER,
    skills CHARACTER VARYING(50)[],
    first_name CHARACTER VARYING(50),
    last_name CHARACTER VARYING(50),
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS public.job
(
    job_id INTEGER GENERATED ALWAYS AS IDENTITY,
    link CHARACTER VARYING(255),
    domain CHARACTER VARYING(255),
    position CHARACTER VARYING(255),
    description TEXT,
    contact_name CHARACTER VARYING(255),
    contact_phone CHARACTER VARYING(20),
    contact_email CHARACTER VARYING(255),
    location CHARACTER VARYING(255),
    post_date DATE,
    company CHARACTER VARYING(255),
    PRIMARY KEY (job_id)
);

CREATE TABLE IF NOT EXISTS public.report
(
    report_id INTEGER GENERATED ALWAYS AS IDENTITY,
    job_id INTEGER,
    summary TEXT,
    skills CHARACTER VARYING(50)[],
    spelling_errors INTEGER,
    grammar_errors INTEGER,
    suspicious_email BOOLEAN,
    suspicious_phone BOOLEAN,
    suspicious_link BOOLEAN,
    ai_risk CHARACTER VARYING(10),
    cumulative_risk CHARACTER VARYING(10),
    PRIMARY KEY (report_id),
    FOREIGN KEY (job_id) REFERENCES public.job (job_id) MATCH SIMPLE
);

CREATE TABLE IF NOT EXISTS public.feedback
(
    email CHARACTER VARYING(255),
    report_id INTEGER,
    feedback TEXT,
    PRIMARY KEY (email, report_id),
    FOREIGN KEY (report_id) REFERENCES public.report (report_id) MATCH SIMPLE
);

CREATE TABLE IF NOT EXISTS public.bookmarks
(
    user_id INTEGER,
    report_id INTEGER,
    PRIMARY KEY (user_id, report_id),
    FOREIGN KEY (user_id) REFERENCES public.user (user_id) MATCH SIMPLE,
    FOREIGN KEY (report_id) REFERENCES public.report (report_id) MATCH SIMPLE
);

END;