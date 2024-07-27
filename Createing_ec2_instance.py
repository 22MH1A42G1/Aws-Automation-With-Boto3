import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create AWS clients
ec2_client = boto3.client('ec2')

def create_ec2_instance():
    try:
        response = ec2_client.run_instances(
            ImageId='ami-0b72821e2f351e396',  # Replace with a valid AMI ID for your region
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='Password'  # Replace with your actual key pair name
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f'EC2 Instance created with Instance ID: {instance_id}')
        
        # Add a name tag to the instance
        ec2_client.create_tags(
            Resources=[instance_id],
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'MyEC2Instance'  # Replace with your desired instance name
                }
            ]
        )
        print(f'EC2 Instance named "MyEC2Instance"')
        
        return instance_id
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error creating EC2 instance: {e}")
        
if __name__ == "__main__":
    create_ec2_instance()
