# 🚀 AWS Automation Dashboard using Python, Boto3, and Streamlit

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Boto3](https://img.shields.io/badge/Boto3-SDK-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

This project is a **fully functional AWS Automation Dashboard**, built using **Streamlit** and **Boto3**, designed to automate infrastructure tasks like launching EC2 instances, uploading files to S3, and managing RDS databases.

✅ Web-based interface for AWS tasks  
✅ Secure .env file for credentials  
✅ Modular structure with clean Python code  
✅ Deployed and tested on Amazon EC2

---

## 🔧 Features

### 🖥️ EC2 Management
- Launch EC2 instance using button click

### ☁️ S3 Management
- Upload files to any S3 bucket from your browser

### 🗃️ RDS Management
- Create, delete RDS instance
- Take and restore snapshots
- Modify database size

---

## 🗂️ Project Structure

```bash
AWS_MINI_PROJECT/
├── app.py                    # Streamlit Web Interface
├── .env                      # AWS keys and configuration
├── EC2/
│   └── create_ec2_instance_file.py
├── RDS/
│   ├── create_rds_instance.py
│   ├── delete_rds_instance.py
│   ├── create_snapshot.py
│   ├── modify_rds_instance.py
│   └── restore_from_snapshot.py
├── S3/
│   └── upload_to_s3.py
├── screenshots/
│   ├── ec2.png
│   ├── s3.png
│   └── rds.png
├── architecture_diagram.png
├── requirements.txt
└── README.md


---

## 🖼️ Architecture Diagram
![Architecture Diagram](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/IMG-20250713-WA0016(1).jpg)
