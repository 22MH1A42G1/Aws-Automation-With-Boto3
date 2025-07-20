# RDS/delete_rds_instance.py

import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

load_dotenv()

def delete_rds_instance():
    rds_client = boto3.client(
        'rds',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )

    try:
        response = rds_client.delete_db_instance(
            DBInstanceIdentifier=os.getenv("RDS_DB_INSTANCE"),
            SkipFinalSnapshot=True
        )
        return f"✅ RDS instance '{response['DBInstance']['DBInstanceIdentifier']}' deletion initiated"
    except NoCredentialsError:
        return "❌ AWS credentials not available"
    except PartialCredentialsError:
        return "❌ Incomplete AWS credentials"
    except Exception as e:
        return f"❌ Error deleting RDS instance: {str(e)}"

if __name__ == "__main__":
    print(delete_rds_instance())