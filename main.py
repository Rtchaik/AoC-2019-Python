import timeit
from Day01.solution import solveDay

startTime = timeit.default_timer()
solveDay()
print('Total time: ', '%6.4f' % (timeit.default_timer() - startTime))
