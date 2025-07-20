# RDS/create_rds_instance.py

import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

load_dotenv()

def create_rds_instance():
    rds_client = boto3.client(
        'rds',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )

    try:
        response = rds_client.create_db_instance(
            DBInstanceIdentifier=os.getenv("RDS_DB_INSTANCE"),
            MasterUsername=os.getenv("RDS_USERNAME"),
            MasterUserPassword=os.getenv("RDS_PASSWORD"),
            DBInstanceClass='db.t3.micro',
            Engine='mysql',
            AllocatedStorage=20
        )
        return f"✅ RDS instance '{response['DBInstance']['DBInstanceIdentifier']}' created successfully"
    except NoCredentialsError:
        return "❌ AWS credentials not available"
    except PartialCredentialsError:
        return "❌ Incomplete AWS credentials"
    except Exception as e:
        return f"❌ Error creating RDS instance: {str(e)}"
