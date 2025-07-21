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
```

---

## 🖼️ Architecture Diagram
[![Architecture Diagram](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/IMG-20250713-WA0016(1).jpg)](https://youtube.com/shorts/NbjEXhEuWSg?si=2nrSsd4KwWbpGvWE)

---
## ⚙️ Setup Instructions (Step-by-Step Guide)

### ✅ 1. Prerequisites

#### Install Python 3.8+ and pip
#### You must have AWS CLI installed and configured with valid credentials.
#### Create an IAM user with the following permissions:
####    - AmazonEC2FullAccess
####    - AmazonS3FullAccess
####    - AmazonRDSFullAccess
#### Ensure an EC2 key pair and valid AMI ID is available in your selected region.

---

### 📁 2. Clone the Repository

# Open terminal or Git Bash and run:
```
git clone https://github.com/22MH1A42G1/Aws-Automation-With-Boto3.git
cd Aws-Automation-With-Boto3
```
---

### 📝 3. Create the .env File

# Create a `.env` file in the root directory and add the following content:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=ap-south-1

AMI_ID=ami-0ded8326293d3201b
KEY_PAIR_NAME=PemKey
EC2_INSTANCE_NAME=MyEC2Instance

RDS_USERNAME=admin
RDS_PASSWORD=Automation123
RDS_DB_INSTANCE=mydbinstance
RDS_SNAPSHOT_NAME=mysnapshot
RDS_RESTORE_INSTANCE=mynewdbinstance

# ⚠️ Make sure to replace the placeholders with your actual AWS values.
# 🚫 DO NOT commit this file to GitHub. Add `.env` to your `.gitignore`.

---

### 📦 4. Install Project Dependencies

# You can install the required libraries using pip:
pip install -r requirements.txt

# Or install manually:
pip install streamlit boto3 python-dotenv

---

### 🧪 5. Run the Application Locally

# Use this command to start your Streamlit app:
streamlit run app.py

# Visit the following URL in your browser:
http://localhost:8501

---

### ☁️ 6. Deploy to AWS EC2 Instance

# Step-by-step deployment on EC2

#### a. Launch an EC2 Instance
# - Select Ubuntu 20.04 or Amazon Linux 2
# - Choose a t2.micro (Free Tier eligible)
# - Create or use an existing Key Pair (PemKey)
# - Allow inbound traffic on port 8501 (Streamlit) and port 22 (SSH)

#### b. Connect to the Instance via SSH

# Run this from your local machine:
ssh -i "PemKey.pem" ec2-user@<EC2-Public-IP>

#### c. Update the instance and install Python

# For Amazon Linux:
sudo yum update -y
sudo yum install python3 git -y

# For Ubuntu:
sudo apt update && sudo apt install python3-pip git -y

#### d. Upload or Clone Your Project

# Option 1: Clone from GitHub (requires your repo to be public or provide access):
git clone https://github.com/yourusername/aws-automation-dashboard.git

# Option 2: Use SCP to upload files:
scp -i PemKey.pem -r ./aws-automation-dashboard ec2-user@<EC2-Public-IP>:~/project

#### e. Navigate to your project directory

cd aws-automation-dashboard

#### f. Recreate .env File

# Paste your .env content again on EC2 manually or upload it via SCP.

#### g. Install Project Requirements on EC2

pip3 install -r requirements.txt

# Or manually:
pip3 install streamlit boto3 python-dotenv

#### h. Run the App on EC2

streamlit run app.py --server.port 8501 --server.enableCORS false

---

### 🌐 7. Access the App in Browser

# Open a browser on your local machine and visit:
http://<EC2-Public-IP>:8501

# 🔓 Make sure port 8501 is open in your EC2 security group settings.

---

### 🧹 8. Clean Up (Optional)

# To avoid unexpected AWS charges:
- Stop or terminate your EC2 instance
- Delete RDS instances and snapshots
- Remove unused S3 files

---

🎉 Done! You have successfully set up the AWS Automation Dashboard.

---

## 📸 Output Screenshots (Evidence)

### 🔐 Before Login
![Before Login Dashboard](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FBefore%20Login%20DashBoard.jpg)

### ✅ After Login
![After Login Dashboard](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FAfter%20Login%20DashBoard.jpg)

---

## 🖥️ EC2 Automation

### ✅ EC2 Instance Launch via Dashboard
![EC2 Launch](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FEC2%20instance%20Launch%20in%20DashBoard.jpg)

### ❌ EC2 Instance Terminated via Dashboard
![EC2 Terminated](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FEC2%20instance%20Terminated%20in%20DashBoard.jpg)

### 🌐 EC2 Deployed Server Screenshot
![EC2 Server Deployed](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FAWS%20EC2%2FAWS%20EC2%20deployment%20Server.jpg)

### 📁 Project Files on EC2 Server
![Project Deployed on EC2](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FAWS%20EC2%2FAWS%20EC2%20Server%20Project%20Files%20Deploy.jpg)

---

## ☁️ S3 Bucket Automation

### 📦 Before Upload (Empty Bucket)
![Empty S3 Bucket](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FAWS%20S3%2FBefore%20Empty%20S3%20Bucket%20AWS.jpg)

### ✅ File Upload via Dashboard
![File Upload Success](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FOutput%20Succussfully%20File%20Uploaded%20in%20S3%20Bucket%20DashBoard.jpg)

### 📁 After File Upload
![After Upload](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FAWS%20S3%2FOutput%20After%20Automation%20S3%20file%20Uploaded%20AWS.jpg)

### ❌ S3 Bucket Deleted
![S3 Deleted](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FClearing%20Project%2FS3%20bucket%20deleted.jpg)

---

## 🗃️ RDS Automation

### ✅ RDS Instance Created
![RDS Created](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FRDS%20database%20created%20DashBoard.jpg)

### 🧩 Snapshot Created
![Snapshot](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FSnapShot%20created%20DashBoard.jpg)

### 📈 DB Instance Modified
![DB Instance Modified](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FModified%20DB%20instance%20class%20DashBoard.jpg)

### ♻️ RDS Restored from Snapshot
![RDS Restored](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FRDS%20Restored%20from%20SnapShot%20DashBoard.jpg)

### ❌ RDS Deletion Initiated
![RDS Deleted](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FHOME%2FRDS%20database%20Deletion%20Initiated%20DashBoard.jpg)

### 🧼 Output: RDS Created
![Output RDS Created](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FRDS%2FOutput%20Succussfully%20Created%20RDS%20database%20in%20AWS.jpg)

### ✅ Output: RDS Modified
![Output DB Modified](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FRDS%2FOutput%20Modified%20DB%20instance%20class%20in%20AWS.jpg)

### 🧹 Output: RDS Deletion
![Output RDS Deleted](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FRDS%2FOutput%20RDS%20database%20Deletion%20Initiated%20AWS.jpg)

### 🔁 Output: RDS Restored
![Output RDS Restored](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FRDS%2FOutput%20Succussfully%20RDS%20Restored%20from%20SnapShot%20AWS.jpg)

---

## 🔒 IAM User Management

### 🧾 IAM User Created with Roles & Access Key
![IAM Roles](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FAWS%20Console%2FIAM%2FIAM%20%28User%20AttachRoles%20AccessKey%29%20AWS.jpg)

### 🧼 IAM User Deleted
![IAM Deleted](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FClearing%20Project%2FIAM%20user%20deleted.jpg)

---

## 🧭 UI Navigation Panels

### 🧠 Project Applications Panel
![Applications Panel](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FProject%20Applications%2FProject%20Applications%20Panel%20DashBoard.jpg)

### 📋 Guidelines Panel
![Guidelines Panel](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FGuideLines%2FGuidelines%20Panel%20DashBoard.jpg)

### 🧭 Navigation Panel
![Navigation Panel](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/NEW%2FDashBoard%2FNavigation%20Panel%20DashBoard.jpg)
