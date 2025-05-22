import os

from .paths import MessagePath


class BotMessage:

    def __init__(self, path: MessagePath):
        self._path = path.value
        self.text = self._read_file()

    def _read_file(self):
        if os.path.isfile(self._path):
            with open(self._path, 'r', encoding='UTF-8') as file:
                return file.read()
        return False

    @classmethod
    def write_file(cls, path: MessagePath, data: str):
        with open(path.value, 'w', encoding='UTF-8') as file:
            file.write(data)
