import json
import boto3
import logging
from datetime import datetime

# Intializes the logger to capture logs. Then we set the logger level to INFO, which will capture all messages with a severity level of INFO or higher.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2=boto3.client('ec2')
    current_date = datetime.now().strftime("%Y-%m-%d")

# Try/Except block used here to attempt to create the snapshot, and if it fails we will receive the Exception error. 
    try:
        response = ec2.create_snapshot(
            VolumeId='vol-04472e77df63e3242',
            Description='My EC2 Snapshot',
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': f"My Ec2 snapshot {current_date}"
                            }
                        ]
                    }
                ]
            )
        logger.info(f"Successfully created snapshot: {json.dumps(response, default=str)}")
    except Exception as e:
        logger.error(f"Error creating snapshot {str(e)}")
