import math

def std(population):
  N = len(population)
  mean = sum(population)/N
  #sum of squared differences between datapoints and the mean
  numerator = sum([(i-mean)**2 for i in population])
  #standard deviation formula
  std = math.sqrt(numerator/N)
  return std

if __name__ == "__main__":
  pop = [2,4,6,8,12,78,12,56,1]
  print('Standard Deviation is {}'.format(std(pop)))