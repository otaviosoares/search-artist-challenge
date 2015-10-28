class ArtistSearcher():
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError('data should be of type list')

        self.__data = data

    def search_by_age(self, minAge, maxAge):
        if minAge <= 0:
            raise ValueError('min age can not be equal or less than 0')

        if maxAge < minAge:
            raise ValueError('max age can not be greater min age')

        def filter_function(x):
            return minAge <= x['age'] <= maxAge

        return filter(filter_function, self.__data)
