from ppadb.client import Client as AdbClient
from ppadb.device import Device

import argparse, sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Shared.prompt import Prompt, Colors

parser = argparse.ArgumentParser(
    prog = 'AdbConnector',
    description = 'AdbEmpire\'s Connector'
)

parser.add_argument('-f', '--file', help = 'Device IP File')

args = parser.parse_args()

ipFilePath = args.file

if not os.path.exists(ipFilePath):
    print('File Not Found.')
    exit(0)

ipFile = open(ipFilePath, 'r')
ips = [ip.strip() for ip in ipFile.readlines()]

ipFile.close()

client = AdbClient(host = '127.0.0.1', port = 5037)

for ip in ips:
    try:
        Prompt.info(f'Connecting To {Colors.blue}{ip}{Colors.end}')

        if client.remote_connect(ip.strip(), 5555):
            device: Device = client.device(f'{ip.strip()}:5555')

            if device:
                Prompt.success(f'Connected To {Colors.green}{ip}{Colors.end}')
            else:
                Prompt.failure(f'Failed To Connect To {Colors.red}{ip}{Colors.end}')
                
    except (KeyboardInterrupt):
        Prompt.info('Exiting Connector!')
        exit(0)