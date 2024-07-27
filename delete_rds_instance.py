import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the RDS client
rds_client = boto3.client('rds')

def delete_rds_instance(instance_identifier):
    try:
        response = rds_client.delete_db_instance(
            DBInstanceIdentifier=instance_identifier,
            SkipFinalSnapshot=True  # Change to False if you want to create a final snapshot
        )
        print(f'RDS instance deleted: {response["DBInstance"]["DBInstanceIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error deleting RDS instance: {e}")

if __name__ == "__main__":
    delete_rds_instance('mydbinstance')
