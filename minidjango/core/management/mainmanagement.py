import re
import sys

from ...utils.colors import Colors
from .commands.runserver import runserver


class ManagementSystem:

    def __init__(self, argv=None):
        self.argv = argv or sys.argv
        self.program_name = self.argv[0]

    def help_text(self):
        help_context = [
            '',
            'Available subcommands:',
            '',
        ]
        command_dict = {
            'staticfiles': ['runserver']
        }

        for title, commands in command_dict.items():
            help_context.append('{}[{}]{}'.format(Colors.RED, title, Colors.RESET))
            for command in commands:
                help_context.append(' ' * 4 + command)
        return '\n'.join(help_context) + '\n'

    def execute(self):
        try:
            subcommand = self.argv[1]
        except:
            subcommand = 'help'


        if subcommand == 'runserver':
            port = 8000
            address = 'localhost'

            try:
                flag = self.argv[2]
            except IndexError:
                pass
            else:
                address_regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
                port_regex = r"^(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[0-5]?[0-9]{0,4})$"
            
                if ':' in flag:
                    colon_index = flag.find(':')
                    address = flag[:colon_index]
                    port = flag[colon_index + 1:]

                    if re.match(address_regex, address) is None:
                        sys.exit(f'{Colors.RED} Address must be a valid address like 187.0.0.1 not {address}\n {Colors.RESET}')
                    elif re.match(port_regex, port) is None:
                        sys.exit(f'{Colors.RED} Port must be a number between 0 and 65535 not {port} \n {Colors.RESET}')
                else:
                    sys.exit('ip:port is not valid.')

            runserver(address, port)
        elif subcommand in ['help', '--help', '-h']:
            sys.stdout.write(self.help_text())
        else:
            sys.stdout.write('Command not found. use manage.py help to get help. \n \n')