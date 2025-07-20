# RDS/restore_from_snapshot.py

import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

load_dotenv()

def restore_from_snapshot():
    rds_client = boto3.client(
        'rds',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )

    try:
        response = rds_client.restore_db_instance_from_db_snapshot(
            DBInstanceIdentifier=os.getenv("RDS_RESTORE_INSTANCE"),
            DBSnapshotIdentifier=os.getenv("RDS_SNAPSHOT_NAME"),
            DBInstanceClass='db.t3.micro'
        )
        return f"✅ RDS instance restored as '{response['DBInstance']['DBInstanceIdentifier']}' from snapshot"
    except NoCredentialsError:
        return "❌ AWS credentials not available"
    except PartialCredentialsError:
        return "❌ Incomplete AWS credentials"
    except Exception as e:
        return f"❌ Error restoring RDS instance: {str(e)}"

if __name__ == "__main__":
    print(restore_from_snapshot())