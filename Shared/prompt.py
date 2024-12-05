from dataclasses import dataclass

from rich.console import Console
from rich.table import Table
from rich.ansi import AnsiDecoder

@dataclass
class Colors:

    purple = '\001\033[0;38;5;141m\002'
    blue = '\001\033[0;38;5;12m\002'
    gray = '\033[90m'
    red = '\001\033[1;31m\002'
    green = '\001\033[38;5;82m\002'
    orange = '\001\033[0;38;5;214m\002'

    underline = '\001\033[4m\002'
    end = '\001\033[0m\002'


@dataclass
class Symbols:
    success = f'{Colors.gray}[{Colors.end}{Colors.green}+{Colors.end}{Colors.gray}]{Colors.end}'
    failure = f'{Colors.gray}[{Colors.end}{Colors.red}-{Colors.end}{Colors.gray}]{Colors.end}'
    info = f'{Colors.gray}[{Colors.end}{Colors.blue}*{Colors.end}{Colors.gray}]{Colors.end}'
    question = f'{Colors.gray}[{Colors.end}{Colors.blue}?{Colors.end}{Colors.gray}]{Colors.end}'

    prompt = f'{Colors.underline}Empire{Colors.end} {Colors.gray}»{Colors.end} '

@dataclass
class Patterns:
    interactive = f'{Colors.gray}[{Colors.blue}%s{Colors.end}{Colors.gray}]{Colors.end} {Colors.underline}Empire{Colors.end} {Colors.gray}»{Colors.end} '

class Prompt:

    promptTitle = Symbols.prompt
    console = Console()
    decoder = AnsiDecoder()

    @staticmethod
    def success(message: str):
        print(f'{Symbols.success} {message}')

    @staticmethod
    def failure(message: str):
        print(f'{Symbols.failure} {message}')

    @staticmethod
    def info(message: str):
        print(f'{Symbols.info} {message}')


    @staticmethod
    def ask(question: str):
        try:
            answer = input(f'{Symbols.question} {question}')
            if (answer.strip() == ''):
                return Prompt.ask(question)
            else:
                return answer
            
        except (KeyboardInterrupt):
            Prompt.info('Exiting...')
            exit(0)

    @staticmethod
    def prompt():
        try:
            userInput = input(f'{Prompt.promptTitle}')
            return userInput
        except (KeyboardInterrupt):
            exitOrNo = Prompt.ask('Are You Sure You Want To Exit? ').lower()
            
            if exitOrNo in ['y', 'yes']:
                exit(0)

    @staticmethod
    def setPrompt(prompt: str):
        Prompt.promptTitle = prompt

    
    @staticmethod
    def showDevices(devices: list) -> None:
        console = Prompt.console
        decoder = Prompt.decoder

        table = Table()

        table.add_column('Ip'); table.add_column('Status')

        for device in devices:

            deviceStatus = f'{Colors.gray}Unknown{Colors.end}'
            try:
                device.get_state()
                deviceStatus = f'{Colors.green}Active{Colors.end}'
            except:
                deviceStatus = f'{Colors.red}Inactive{Colors.end}'

            table.add_row(decoder.decode_line(f'{Colors.blue}{device.serial.split(':')[0]}{Colors.end}'), decoder.decode_line(deviceStatus))

        console.print(table)
