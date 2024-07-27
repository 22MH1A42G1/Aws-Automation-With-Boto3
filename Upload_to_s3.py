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
