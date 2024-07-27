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
