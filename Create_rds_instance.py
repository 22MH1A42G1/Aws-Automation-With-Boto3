import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create AWS clients
rds_client = boto3.client('rds')

def create_rds_instance():
    try:
        response = rds_client.create_db_instance(
            DBInstanceIdentifier='mydbinstance',
            MasterUsername='admin',
            MasterUserPassword='Iship-31',  # Replace with a secure password
            DBInstanceClass='db.t3.micro',  # Use a supported DB instance class
            Engine='mysql',
            AllocatedStorage=20
        )
        print(f'RDS instance created: {response["DBInstance"]["DBInstanceIdentifier"]}')
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error creating RDS instance: {e}")
        
if __name__ == "__main__":
    create_rds_instance()
