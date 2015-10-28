import json


class ArtistLoader():
    def __init__(self, path):
        with open(path) as f:
            file_content = f.read()
            self.__data = json.loads(file_content)

    @property
    def data(self):
        return self.__data
