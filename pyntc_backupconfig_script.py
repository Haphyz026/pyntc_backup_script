import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='192.168.122.226', username='hafiz', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()
ios_run = iosvl2.running_config
print (ios_run)
