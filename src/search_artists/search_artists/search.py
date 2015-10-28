class Search():
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError('data should be of type list')

        self.__data = data

    def search(self, minVal, maxVal):
        def filter_function(x):
            return x['age'] >= minVal and x['age'] <= maxVal

        return filter(filter_function, self.__data)
