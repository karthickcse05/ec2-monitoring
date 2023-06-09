import boto3
import json

#change to the region you are looking up
region='us-east-1'
client = boto3.client('ec2',region_name=region)

instance_file = r'instanceId_Input.txt'
instances = []


instanceDetails = client.describe_instances()
## print(instanceDetails)
with(open(instance_file,'w')) as out:
    for instance in instanceDetails['Reservations']:
        out.write(str(instance['Instances'][0]['InstanceId'])+'\n')

with(open(instance_file)) as fileIn:
    for line in fileIn:
        instances.append(line.strip())
print(instances)   
instanceDetails = client.monitor_instances(InstanceIds=instances)
