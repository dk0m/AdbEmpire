from Shared.prompt import Prompt, Colors
from Empire.empire import Empire

empire = Empire(Prompt)

def displayLogo():
    print(f'''{Colors.blue}
┌─┐  ┌┬┐  ┌┐   ┌─┐  ┌┬┐  ┌─┐  ┬  ┬─┐  ┌─┐
├─┤   ││  ├┴┐  ├┤   │││  ├─┘  │  ├┬┘  ├┤ 
┴ ┴  ─┴┘  └─┘  └─┘  ┴ ┴  ┴    ┴  ┴└─  └─┘
{Colors.end}''')
    
displayLogo()

Prompt.info(f'Found {Colors.blue}{empire.deviceCount}{Colors.end} Devices!')

while True:
    userInput = Prompt.prompt()
    
    if (not userInput):
        continue
    
    if (userInput == ''):
        continue

    empire.handleUserCmd(userInput)