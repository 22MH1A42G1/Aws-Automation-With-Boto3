import boto3
import os
from dotenv import load_dotenv

# Load credentials from .env if present
load_dotenv()

def delete_ec2_instance(instance_id, region='ap-south-1'):
    """
    Terminates the EC2 instance with the specified instance ID.

    Args:
        instance_id (str): The ID of the EC2 instance to terminate.
        region (str): The AWS region. Default is 'ap-south-1'.

    Returns:
        dict: The response from the terminate_instances call.
    """
    # Create EC2 client using explicit credentials
    ec2 = boto3.client(
        'ec2',
        region_name=region,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    try:
        response = ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"✅ Terminating instance: {instance_id}")
        return response
    except Exception as e:
        print(f"❌ Error terminating instance {instance_id}: {e}")
        return None

if __name__ == "__main__":
    instance_id = input("Enter the instance ID you want to terminate (e.g., i-xxxxxxxxxxxxxxxxx): ")
    if not instance_id.startswith("i-"):
        print("❌ Invalid instance ID. It must start with 'i-'.")
    else:
        delete_ec2_instance(instance_id)
