import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the RDS client
rds_client = boto3.client('rds')

def modify_rds_instance(instance_identifier, new_instance_class):
    try:
        response = rds_client.modify_db_instance(
            DBInstanceIdentifier=instance_identifier,
            DBInstanceClass=new_instance_class,
            ApplyImmediately=True
        )
        print(f'RDS instance modified: {response["DBInstance"]["DBInstanceIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error modifying RDS instance: {e}")
        
if __name__ == "__main__":
    modify_rds_instance('mydbinstance', 'db.t3.small')
