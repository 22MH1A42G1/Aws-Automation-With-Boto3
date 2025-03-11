
# 🚀 AWS Automation with Boto3 (Python)

## 📹 Final Output  
[![Watch the video](https://img.youtube.com/vi/B6vLrTkUHzs/0.jpg)](https://www.youtube.com/watch?v=B6vLrTkUHzs)

## 📌 Table of Contents  
- [Introduction](#introduction)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Creating an EC2 Instance](#creating-an-ec2-instance)  
  - [Uploading a File to S3 Bucket](#uploading-a-file-to-s3-bucket)  
  - [Creating an RDS Instance](#creating-an-rds-instance)  
  - [Modifying an RDS Instance](#modifying-an-rds-instance)  
  - [Creating a Snapshot](#creating-a-snapshot)  
  - [Restoring from a Snapshot](#restoring-from-a-snapshot)  
  - [Deleting an RDS Instance](#deleting-an-rds-instance)  
- [Cleaning AWS Environment](#cleaning-aws-environment)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 📝 Introduction  
This project provides a Python script that leverages the AWS SDK for Python (Boto3) to automate several common AWS tasks. The tasks covered by this script include:  

✅ Provisioning EC2 instances  
✅ Uploading files to S3  
✅ Managing RDS databases  

This script simplifies AWS resource management through automation.

---

## ⚙️ Prerequisites  
Ensure you meet the following requirements:  
- ✅ AWS account  
- ✅ Python 3.6 or later installed  
- ✅ Boto3 installed  
- ✅ AWS credentials configured  
- ✅ Using AWS Cloud9 IDE environment  

---

## 🛠 Installation  
To install Boto3, run:  
```sh
pip install boto3
```

---

## 🚀 Usage  
To run any script, use:  
```sh
python3 file_name.py
```
Replace `file_name.py` with the actual script name.

---

### 🌐 Creating an EC2 Instance  
```python
import boto3

ec2_client = boto3.client('ec2')

def create_ec2_instance():
    response = ec2_client.run_instances(
        ImageId='ami-0b72821e2f351e396', 
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='YourKeyPair'
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f'EC2 Instance created with ID: {instance_id}')

if __name__ == "__main__":
    create_ec2_instance()
```
Run:  
```sh
python3 create_ec2_instance.py
```

---

### ☁️ Uploading a File to S3 Bucket  
```python
import boto3

s3_client = boto3.client('s3')

def upload_to_s3(bucket_name, file_name):
    s3_client.upload_file(file_name, bucket_name, file_name)
    print(f'File {file_name} uploaded to {bucket_name}')

if __name__ == "__main__":
    upload_to_s3('your-bucket-name', 'your-file.txt')
```
Run:  
```sh
python3 upload_to_s3.py
```

---

### 🗄 Creating an RDS Instance  
```python
import boto3

rds_client = boto3.client('rds')

def create_rds_instance():
    response = rds_client.create_db_instance(
        DBInstanceIdentifier='mydbinstance',
        MasterUsername='admin',
        MasterUserPassword='YourSecurePassword',
        DBInstanceClass='db.t3.micro',
        Engine='mysql',
        AllocatedStorage=20
    )
    print(f'RDS Instance Created: {response["DBInstance"]["DBInstanceIdentifier"]}')

if __name__ == "__main__":
    create_rds_instance()
```
Run:  
```sh
python3 create_rds_instance.py
```

---

### ✏️ Modifying an RDS Instance  
```python
import boto3

rds_client = boto3.client('rds')

def modify_rds_instance(instance_identifier, new_instance_class):
    response = rds_client.modify_db_instance(
        DBInstanceIdentifier=instance_identifier,
        DBInstanceClass=new_instance_class,
        ApplyImmediately=True
    )
    print(f'RDS Instance Modified: {response["DBInstance"]["DBInstanceIdentifier"]}')

if __name__ == "__main__":
    modify_rds_instance('mydbinstance', 'db.t3.small')
```
Run:  
```sh
python3 modify_rds_instance.py
```

---

### 📸 Creating a Snapshot  
```python
import boto3

rds_client = boto3.client('rds')

def create_snapshot(instance_identifier, snapshot_identifier):
    response = rds_client.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceIdentifier=instance_identifier
    )
    print(f'Snapshot Created: {response["DBSnapshot"]["DBSnapshotIdentifier"]}')

if __name__ == "__main__":
    create_snapshot('mydbinstance', 'mysnapshot')
```
Run:  
```sh
python3 create_snapshot.py
```

---

### 🔄 Restoring from a Snapshot  
```python
import boto3

rds_client = boto3.client('rds')

def restore_from_snapshot(snapshot_identifier, new_instance_identifier):
    response = rds_client.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=new_instance_identifier,
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceClass='db.t3.micro'
    )
    print(f'RDS Instance Restored: {response["DBInstance"]["DBInstanceIdentifier"]}')

if __name__ == "__main__":
    restore_from_snapshot('mysnapshot', 'mynewdbinstance')
```
Run:  
```sh
python3 restore_from_snapshot.py
```

---

### ❌ Deleting an RDS Instance  
```python
import boto3

rds_client = boto3.client('rds')

def delete_rds_instance(instance_identifier):
    response = rds_client.delete_db_instance(
        DBInstanceIdentifier=instance_identifier,
        SkipFinalSnapshot=True
    )
    print(f'RDS Instance Deleted: {response["DBInstance"]["DBInstanceIdentifier"]}')

if __name__ == "__main__":
    delete_rds_instance('mydbinstance')
```
Run:  
```sh
python3 delete_rds_instance.py
```

---

## 🧹 Cleaning AWS Environment  
To clean up AWS resources after the project:  
1. **Delete IAM roles and credentials** used for the project.  
2. **Delete EC2 instances** created by the project.  
3. **Delete S3 buckets and files** related to the project.  
4. **Delete the RDS database** used in the project.  

---

## 🤝 Contributing  
Contributions are welcome! Fork this repository and submit a pull request.  

---

## 📜 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

🔗 **Follow me on GitHub:** [@22MH1A42G1](https://github.com/22MH1A42G1)  
📧 **Contact me:** [LinkedIn](https://www.linkedin.com/in/aditya-indana-899734216)  
```
