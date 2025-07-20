import boto3, os
from dotenv import load_dotenv
from botocore.exceptions import *

load_dotenv()

def create_ec2_instance():
    ec2 = boto3.client('ec2',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION'))

    try:
        response = ec2.run_instances(
            ImageId=os.getenv("AMI_ID"),
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName=os.getenv("KEY_PAIR_NAME")
        )
        instance_id = response['Instances'][0]['InstanceId']
        ec2.create_tags(Resources=[instance_id],
            Tags=[{'Key': 'Name', 'Value': os.getenv("EC2_INSTANCE_NAME")}])
        return f"✅ EC2 Instance Created: {instance_id}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    print(create_ec2_instance())