from solution.solution import Solution

some_files = ['small.txt']
for file in some_files:
    solver = Solution(filename=file)
    print(f"In file '{file}'\n")
    print(f'sum = {solver.sum()}\nproduct = {solver.product()}\n'
          f'minimum = {solver.find_minimum()}\nmaximum = {solver.find_maximum()}\n'
          )

