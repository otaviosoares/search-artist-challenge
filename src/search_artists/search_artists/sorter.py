class MedianSorter():
    def __init__(self, median):
        self.__median = median

    def __call__(self, value1, value2):
        v1 = value1['age']
        v2 = value2['age']
        return -1 if abs(self.__median - v1) < abs(self.__median - v2) else 1
