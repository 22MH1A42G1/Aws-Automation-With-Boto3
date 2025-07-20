# S3/upload_to_s3.py

import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

load_dotenv()

def upload_to_s3(bucket_name, file_name, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        return f"✅ File '{file_name}' uploaded to S3 bucket '{bucket_name}' as '{object_name}'"
    except FileNotFoundError:
        return f"❌ File '{file_name}' not found locally"
    except NoCredentialsError:
        return "❌ AWS credentials not available"
    except PartialCredentialsError:
        return "❌ Incomplete AWS credentials"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    bucket = input("Enter the S3 bucket name: ")
    file_to_upload = input("Enter the path to the file you want to upload: ")
    object_name = input("Enter the S3 object name (or press Enter to use the file name): ") or None
    print(upload_to_s3(bucket, file_to_upload, object_name))