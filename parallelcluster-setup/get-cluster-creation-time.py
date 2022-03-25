from datetime import datetime
import sys

if len(sys.argv) < 2:
    print('Error: no time stamp was found\n')
    sys.exit(1)
else:
    creation_time_obj = datetime.strptime(sys.argv[1], '%Y-%m-%dT%H:%M:%S.%fZ')
    print(creation_time_obj.strftime('%Y%m%d%H%M'))