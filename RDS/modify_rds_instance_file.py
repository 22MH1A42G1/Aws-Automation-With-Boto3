# RDS/modify_rds_instance.py

import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

load_dotenv()

def modify_rds_instance(new_instance_class):
    rds_client = boto3.client(
        'rds',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )

    try:
        response = rds_client.modify_db_instance(
            DBInstanceIdentifier=os.getenv("RDS_DB_INSTANCE"),
            DBInstanceClass=new_instance_class,
            ApplyImmediately=True
        )
        return f"✅ RDS instance '{response['DBInstance']['DBInstanceIdentifier']}' modified to class '{new_instance_class}'"
    except NoCredentialsError:
        return "❌ AWS credentials not available"
    except PartialCredentialsError:
        return "❌ Incomplete AWS credentials"
    except Exception as e:
        return f"❌ Error modifying RDS instance: {str(e)}"

if __name__ == "__main__":
    new_class = input("Enter the new DB instance class (e.g., db.t3.micro): ")
    print(modify_rds_instance(new_class))