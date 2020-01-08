import numpy

original_grid = [['.', '.', '.', '.', '.', '.'],
                 ['.', 'O', 'O', '.', '.', '.'],
                 ['O', 'O', 'O', 'O', '.', '.'],
                 ['O', 'O', 'O', 'O', 'O', '.'],
                 ['.', 'O', 'O', 'O', 'O', 'O'],
                 ['O', 'O', 'O', 'O', 'O', '.'],
                 ['O', 'O', 'O', 'O', '.', '.'],
                 ['.', 'O', 'O', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.']]

def print_grid(grid):
  for x in grid:
    for y in x:
      print(y, end=' ')
    print('')
  print('\n')

print('Original grid:')
print_grid(original_grid)

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.rot90.html
# Args: input array, number of times to rotate by 90 degrees.
numpy_grid = numpy.rot90(original_grid, k=3)
print('numpy grid:')
print_grid(numpy_grid)

loop_grid = []

# original_grid is a list of lists -- start with first list and append the
# first value. Then iterate by going to the first value of the second list,
# and so on. Use a loop within a loop to do this.
for i in range(len(original_grid[0])):
  loop_grid.append([x[i] for x in original_grid])
print('Loop grid:')
print_grid(loop_grid)