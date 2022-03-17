import yaml
import sys

if len(sys.argv) < 2:
    print('invalid argument. Usage:\n\tget-compute-instance-type.py [config_file].yaml\n')
    sys.exit(1)
with open(sys.argv[1], 'r') as file:
    config = yaml.safe_load(file)
print(config['Scheduling']['SlurmQueues'][0]['ComputeResources'][0]['InstanceType'])
