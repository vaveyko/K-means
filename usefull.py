import numpy as np

def distance(first, second):
    return np.sqrt((first[0] - second[0])**2 + (first[1] - second[1])**2)

def is_equal(first, second):
    delta = 0.01
    return second - delta < first < second + delta

class DotsClass:
    def __init__(self, kernel):
        self.__dots = []
        self.__kernel = kernel

    def add_dot(self, elem):
        self.__dots.append(elem)

    def clear_dot(self):
        self.__dots.clear()

    def get_dots(self):
        return np.array(self.__dots)

    def get_kernel(self):
        return self.__kernel

    def set_kernel(self, kernel):
        self.__kernel = kernel
