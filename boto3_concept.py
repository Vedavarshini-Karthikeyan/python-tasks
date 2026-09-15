#To create a resources in AWS
import boto3
client = boto3.client('s3')
response = client.create_bucket(
    bucket = "veda-15092026"
)

#To get the existing resources
response = client.get_bucket_acl(
    bucket = "veda-10092026"
)