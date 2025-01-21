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
            runserver()
        elif subcommand in ['help', '--help', '-h']:
            sys.stdout.write(self.help_text())
        else:
            sys.stdout.write('Command not found. use manage.py help to get help. \n \n')