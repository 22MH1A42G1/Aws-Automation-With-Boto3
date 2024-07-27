import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the RDS client
rds_client = boto3.client('rds')

def create_snapshot(instance_identifier, snapshot_identifier):
    try:
        response = rds_client.create_db_snapshot(
            DBSnapshotIdentifier=snapshot_identifier,
            DBInstanceIdentifier=instance_identifier
        )
        print(f'Snapshot created: {response["DBSnapshot"]["DBSnapshotIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error creating snapshot: {e}")
        
if __name__ == "__main__":
    create_snapshot('mydbinstance', 'mysnapshot')
