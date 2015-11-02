import operator


class ArtistSearcher():
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError('data should be of type list')
        data.sort()
        self.__data = data

    def search_by_age(self, minAge, maxAge, sorterKlass=None):
        if minAge <= 0:
            raise ValueError('min age can not be equal or less than 0')

        if maxAge < minAge:
            raise ValueError('max age can not be greater min age')

        def filter_function(x):
            return minAge <= x['age'] <= maxAge

        result = filter(filter_function, self.__data)

        if sorterKlass:
            min_age = min(result, key=operator.itemgetter('age'))['age']
            max_age = max(result, key=operator.itemgetter('age'))['age']
            median = (min_age + max_age) / 2
            sorter = sorterKlass(median)
            result.sort(sorter)
        return result
