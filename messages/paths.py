from enum import Enum

import os


class MessagePath(Enum):
    START = os.path.join('messages', 'start.txt')
    RULES = os.path.join('messages', 'rules.txt')
    HELP = os.path.join('messages', 'help.txt')
