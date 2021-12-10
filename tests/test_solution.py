import sys
sys.path.insert(0, "../solution")
import solution
import unittest


class SolutionTestCase(unittest.TestCase):

    def test_minimum(self):
        numbers = ['3', '0', '1', '2', '0', '4', '5', '-1', '10']
        with open('test_minimum.txt', 'w') as file:
            file.write(' '.join(numbers))
        solver = solution.Solution('test_minimum.txt')
        self.assertEqual(-1, solver.find_minimum())

    def test_maximum(self):
        numbers = ['3', '20', '1', '2', '0', '4', '5', '-1', '10']
        with open('test_maximum.txt', 'w') as file:
            file.write(' '.join(numbers))
        solver = solution.Solution('test_maximum.txt')
        self.assertEqual(20, solver.find_maximum())

    def test_sum(self):
        numbers = ['999', '-999', '0', '1']
        with open('test_sum.txt', 'w') as file:
            file.write(' '.join(numbers))
        solver = solution.Solution('test_sum.txt')
        self.assertEqual(1, solver.sum())

    def test_product(self):
        numbers = ['-3', '4', '-1', '-1', '-1', '2']
        with open('test_product.txt', 'w') as file:
            file.write(' '.join(numbers))
        solver = solution.Solution('test_product.txt')
        self.assertEqual(24, solver.product())
