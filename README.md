# 🧠 SmartHiringApp

> An intelligent resume ranking and hiring platform built with Django — leveraging NLP and ML to match candidates to job descriptions automatically.

![Django](https://img.shields.io/badge/Django-web_framework-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=flat-square&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Elastic_Beanstalk-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-database-003B57?style=flat-square&logo=sqlite&logoColor=white)

---

## 📖 Overview

SmartHiringApp is a cloud-deployed Django web application that automates resume screening and candidate ranking. Built as a Fall 2017 Cloud Computing course project, it uses NLP-based resume parsing and scoring to rank applicants against job descriptions — reducing recruiter workload dramatically.

## ✨ Features

- **Resume Ranking Engine** — NLP-powered scoring of resumes against job descriptions
- **Web Interface** — Clean Django UI for uploading and reviewing candidates
- **Cloud Deployment** — Deployed on AWS Elastic Beanstalk (`.ebextensions` config included)
- **Research Backed** — Includes full LaTeX research paper (`results.tex`) and PDF report on model performance
- **SQLite Backend** — Lightweight database for candidate and job data

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| ML / NLP | Resume ranking algorithms (resumeranking module) |
| Database | SQLite3 |
| Deployment | AWS Elastic Beanstalk |
| Research | LaTeX, PDF report |

## 🚀 Quick Start

```bash
# Install dependencies
pip install django

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver

# Visit http://127.0.0.1:8000
```

## 📂 Repo Structure

```
├── manage.py                # Django entry point
├── finalproject/            # Django project settings
├── resumeranking/           # Core resume ranking ML module
├── static/                  # Static assets (CSS, JS)
├── db.sqlite3               # SQLite database
├── .ebextensions/           # AWS Elastic Beanstalk config
├── results.tex              # LaTeX research paper
└── results.pdf              # Compiled research report
```

## 📊 Research

This project is accompanied by a full research paper evaluating the resume ranking model's performance, including precision/recall metrics across multiple candidate datasets. See `results.pdf` for the full report.

---

<p align="center">Made with ❤️ by <a href="https://github.com/durveshvedak">Durvesh Vedak</a></p>
