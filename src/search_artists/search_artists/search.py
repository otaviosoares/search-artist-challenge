class Search():
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError('data should be of type list')

        self.__data = data
