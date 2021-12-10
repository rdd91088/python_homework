from math import inf
from functools import reduce


class Solution:

    __slots__ = ['_filename']

    def __init__(self, filename):
        self._filename = filename

    def find_minimum(self):
        res = inf
        with open(self._filename, 'r') as file:
            for line in file:
                res = min(res, min(map(int, line.rsplit())))
        return res

    def find_maximum(self):
        res = -inf
        with open(self._filename, 'r') as file:
            for line in file:
                res = max(res, max(map(int, line.rsplit())))
        return res

    def sum(self):
        res = 0
        with open(self._filename, 'r') as file:
            for line in file:
                res += sum(map(int, line.rsplit()))
        return res

    def product(self):
        res = 1
        with open(self._filename, 'r') as file:
            for line in file:
                res *= reduce(lambda x, y: x * y, (map(int, line.rsplit())))
        return res
