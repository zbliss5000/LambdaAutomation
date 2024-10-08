import boto3
# defining our entry point for the function here, and then specifying the resource we will be using.
def lambda_handler(event, context):
    ec2_resource = boto3.resource('ec2')
    
    # for loop being used here, that will check all elastic IPs in our VPC addresses, and release any that do not have an instance ID associated.
    for elastic_ip in ec2_resource.vpc_addresses.all():
        if elastic_ip.instance_id is None:
            print(f"\nNo assocciation for elastic IP: {elastic_ip}. Releasing...\n")
            elastic_ip.release()
    # returns a HTTP status code 200 for succesful release
    return {
        'statusCode': 200,
        'body': 'Processed elastic IPs.'
    }