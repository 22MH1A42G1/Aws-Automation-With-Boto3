import boto3, os
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

ec2 = boto3.client(
    'ec2',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)

try:
    ec2.describe_regions()
    print("✅ Credentials are valid")
except ClientError as e:
    print("❌ Auth error:", e)
