from toml import load
from shodan import Shodan
from argparse import ArgumentParser

parser = ArgumentParser(
    prog = 'AdbEmpire Scanner',
    description = 'Utility Scanner For ADB Devices.',
)

parser.add_argument('-f', '--fullscan', action = 'store_true', help = 'Scan For ALL ADB Devices?')
parser.add_argument('-o', '--output', help = 'Output File Path')

args = parser.parse_args()

fullScan = args.fullscan
outputFilePath = args.output
query = 'android+debug+bridge'

config = load('Config.toml')
shodanConfig = config['shodan']

shodan = Shodan(key = shodanConfig['key'])
results = shodan.search(query, page = 100)['matches']

outputFile = open(outputFilePath, 'a')

if fullScan:
    results = shodan.search_cursor(query)
    for index, result in enumerate(results):
        ip = result['ip_str']
        outputFile.write(f'{ip}\n')
        print(f"\r[+] Wrote ADB Scan Result #{index}", end = '', flush = True)
else:
    results = shodan.search(query, page = 100)['matches']
    for result in results:
        ip = result['ip_str']
        outputFile.write(f'{ip}\n')

    print(f"[+] Fetched The First 100 ADB Devices.")
    
outputFile.close()