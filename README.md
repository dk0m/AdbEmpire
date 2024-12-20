
# AdbEmpire

A Simple Python Command And Control For ADB Devices.

## Structure & Usage
The project is mainly divided into 3 parts, The scanner, The connector and AdbEmpire itself.

The scanner scans for ADB devices using Shodan's API, Once It has found some devices, It stores their IPs in a file for later use by the connector.

The connector goes through each single line in the IPs file generated by the Scanner and tries to connect to each device, The Connector will only work if the ADB server is running locally, If you aren't sure if it's running or not, Run this command:
```
adb server
```

AdbEmpire will simply just go through all the devices The connector has connected to and will allow the user to interact with each device as long as it's active.

To see how to use both the connector and the scanner, Run the help command for them.

To start AdbEmpire, Run this in the root directory of the project.
```
python main.py
```

## Example Output
```
Empire » devices

┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Ip              ┃ Status   ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ 112.164.117.176 │ Inactive │
│ 114.55.4.232    │ Inactive │
│ 121.172.57.100  │ Active   │
│ 121.190.31.103  │ Inactive │
│ 123.7.117.72    │ Active   │
│ 123.7.117.81    │ Active   │
│ 137.118.139.161 │ Inactive │
│ 14.55.174.157   │ Inactive │
│ 180.69.156.113  │ Inactive │
│ 190.198.194.4   │ Inactive │
│ 220.117.128.167 │ Inactive │
│ 220.122.59.249  │ Inactive │
│ 222.104.166.238 │ Inactive │
│ 222.168.178.99  │ Active   │
│ 222.67.149.129  │ Active   │
│ 45.21.197.7     │ Inactive │
│ 47.189.175.82   │ Inactive │
│ 47.53.169.35    │ Inactive │
│ 59.12.169.9     │ Inactive │
│ 73.144.249.204  │ Active   │
│ 81.198.151.92   │ Inactive │
│ 83.227.232.16   │ Inactive │
└─────────────────┴──────────┘
```

## Software Requirements
This project requires the user to have the Android ADB tools installed and added to PATH, You can download them off the official Android Studio site.

## Todo
- Organize codebase
- Save path once the change directory command is used
- Add more features
