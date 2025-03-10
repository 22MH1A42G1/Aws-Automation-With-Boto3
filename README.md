### AWS Automation with Boto3 (Python)

#### Short Description
Python Script for AWS Automation with Boto3. This script automates common AWS tasks such as provisioning EC2 instances, uploading files to S3, and managing RDS databases.

<video src="video.mp4" controls width="600"></video>
📽️ [![Watch the video](https://www.whizlabs.com/blog/wp-content/uploads/2020/09/aws-automation-using-python-and-boto3.png)](https://github.com/22MH1A42G1/Aws-Automation-With-Boto3/blob/main/Automation(Ec2&S3&RDS).mp4)


#### Table of Contents
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
- [Contributing](#contributing)
- [License](#license)

#### Introduction
This project provides a Python script that leverages the AWS SDK for Python (Boto3) to automate several common AWS tasks. The tasks covered by this script include provisioning EC2 instances, uploading files to S3 buckets, and managing RDS databases. This script aims to simplify the process of managing AWS resources through automation.

#### Prerequisites
Before you begin, ensure you have met the following requirements:
- You have an AWS account.
- You have installed Python 3.6 or later.
- You have installed Boto3.
- You have configured your AWS credentials.
- You are using AWS Cloud9 IDE environment.

#### Installation
To install Boto3, run the following command in your Cloud9 terminal:
```sh
pip install boto3
```

#### Usage

To run any of the Python scripts provided in this project, use the following command in your Cloud9 terminal:
```sh
python3 file_name.py
```
Replace `file_name.py` with the actual name of the Python file you want to execute.

##### Creating an EC2 Instance
```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create AWS clients
ec2_client = boto3.client('ec2')

def create_ec2_instance():
    try:
        response = ec2_client.run_instances(
            ImageId='ami-0b72821e2f351e396',  # Replace with a valid AMI ID for your region
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='Password'  # Replace with your actual key pair name
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f'EC2 Instance created with Instance ID: {instance_id}')
        
        # Add a name tag to the instance
        ec2_client.create_tags(
            Resources=[instance_id],
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'MyEC2Instance'  # Replace with your desired instance name
                }
            ]
        )
        print(f'EC2 Instance named "MyEC2Instance"')
        
        return instance_id
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error creating EC2 instance: {e}")
        
if __name__ == "__main__":
    create_ec2_instance()
```

To run the EC2 instance creation script:
```sh
python3 create_ec2_instance.py
```

##### Uploading a File to S3 Bucket
```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create AWS clients
s3_client = boto3.client('s3')

def upload_to_s3(bucket_name, file_name, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f'File {file_name} uploaded to {bucket_name}/{object_name}')
    except FileNotFoundError:
        print(f'The file {file_name} was not found')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
    
if __name__ == "__main__":
    upload_to_s3('iship-bucket', 'SystemLogo.bmp')
```

To run the S3 upload script:
```sh
python3 upload_to_s3.py
```

##### Creating an RDS Instance
```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create AWS clients
rds_client = boto3.client('rds')

def create_rds_instance():
    try:
        response = rds_client.create_db_instance(
            DBInstanceIdentifier='mydbinstance',
            MasterUsername='admin',
            MasterUserPassword='Iship-31',  # Replace with a secure password
            DBInstanceClass='db.t3.micro',  # Use a supported DB instance class
            Engine='mysql',
            AllocatedStorage=20
        )
        print(f'RDS instance created: {response["DBInstance"]["DBInstanceIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error creating RDS instance: {e}")
        
if __name__ == "__main__":
    create_rds_instance()
```

To run the RDS instance creation script:
```sh
python3 create_rds_instance.py
```

##### Modifying an RDS Instance
```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the RDS client
rds_client = boto3.client('rds')

def modify_rds_instance(instance_identifier, new_instance_class):
    try:
        response = rds_client.modify_db_instance(
            DBInstanceIdentifier=instance_identifier,
            DBInstanceClass=new_instance_class,
            ApplyImmediately=True
        )
        print(f'RDS instance modified: {response["DBInstance"]["DBInstanceIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error modifying RDS instance: {e}")
        
if __name__ == "__main__":
    modify_rds_instance('mydbinstance', 'db.t3.small')
```

To run the RDS instance modification script:
```sh
python3 modify_rds_instance.py
```

##### Creating a Snapshot
```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the RDS client
rds_client = boto3.client('rds')

def create_snapshot(instance_identifier, snapshot_identifier):
    try:
        response = rds_client.create_db_snapshot(
            DBSnapshotIdentifier=snapshot_identifier,
            DBInstanceIdentifier=instance_identifier
        )
        print(f'Snapshot created: {response["DBSnapshot"]["DBSnapshotIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error creating snapshot: {e}")
        
if __name__ == "__main__":
    create_snapshot('mydbinstance', 'mysnapshot')
```

To run the snapshot creation script:
```sh
python3 create_snapshot.py
```

##### Restoring from a Snapshot
```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the RDS client
rds_client = boto3.client('rds')

def restore_from_snapshot(snapshot_identifier, new_instance_identifier):
    try:
        response = rds_client.restore_db_instance_from_db_snapshot(
            DBInstanceIdentifier=new_instance_identifier,
            DBSnapshotIdentifier=snapshot_identifier,
            DBInstanceClass='db.t3.micro',  # Use a supported DB instance class
        )
        print(f'RDS instance restored: {response["DBInstance"]["DBInstanceIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error restoring RDS instance: {e}")
        
if __name__ == "__main__":
    restore_from_snapshot('mysnapshot', 'mynewdbinstance')
```

To run the snapshot restoration script:
```sh
python3 restore_from_snapshot.py
```

##### Deleting an RDS Instance
```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the RDS client
rds_client = boto3.client('rds')

def delete_rds_instance(instance_identifier):
    try:
        response = rds_client.delete_db_instance(
            DBInstanceIdentifier=instance_identifier,
            SkipFinalSnapshot=True  # Change to False if you want to create a final snapshot
        )
        print(f'RDS instance deleted: {response["DBInstance"]["DBInstanceIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error deleting RDS instance: {e}")

if __name__ == "__main__":
    delete_rds_instance('mydbinstance')
```

To run the RDS instance deletion script:
```sh
python3 delete_rds_instance.py
```

#### Contributing
Contributions are

 welcome! Please fork this repository and submit a pull request.

#### License
This project is licensed under the MIT License. See the LICENSE file for details.
