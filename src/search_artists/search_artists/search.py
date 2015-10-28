class Search():
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError('data should be of type list')

        self.__data = data

    def search(self, minVal, maxVal):
        if minVal <= 0:
            raise ValueError('min value can not be equal or less than 0')

        def filter_function(x):
            return x['age'] >= minVal and x['age'] <= maxVal

        return filter(filter_function, self.__data)
