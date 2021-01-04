"""
What is Mean, Median, and Mode?

Mean:
The average of the set of numbers is called Mean. In laymen's terms, you get the mean when the sum of the numbers in the set is divided by the length of the set.

Example: 
set = (2,6,3,8,3,6), n = length of the set = 6
Mean = (2+6+3+8+3+6)/6

Weighted Mean:
You get the weighted mean when the sum of the product of each number in the set and its weight is divided by the sum of the weights.

Example: 
set = (2,6,3,8,3,6), weights = (1,8,4,7,6,2)
Weighted Mean = (2x1)+(6x8)+(3x4)+(8x7)+(3x6)+(6x2)/(1+8+4+7+6+2)

Median:
Median is used to find the center of the set of numbers or dataset. 

If the length of the set is an odd number, the value in the center, after sorting, is the median. Moreover, if the length is an even number, the value, after 
summing up the two values in the center (after sorting) and dividing them by 2, is the median.

Example: set = (4,1,9,7,1) - length is odd, 
sorted set = (1,1,4,7,9), Median = 4

set = (4,1,9,7,1,10) - length is even,
sorted set = (1,1,4,7,9,10), Median = (4+7)/2 = 5.5

Mode:
The number that occurs more than one time in the set is the Mode. 

If the frequency of two or more numbers is the same then all of those numbers are modes. If none of the numbers are repeated then all the numbers in the set are 
valid modes.

Example: set = (1,1,4,7,9), 
Mode = 1

set = (1,2,4,7,9), 
Each number is a valid mode.
----

Usage:

Mean: The mean is used to get a typical value of the various observations and an insight of the dataset with similar numerical values. For instance, we can use 
mean to find out how many hours an employee has spent on an unofficial break every day. Moreover, the weighted mean is used when we consider every value in the 
set with different importance.

Median: The median is used when the mean is unable to provide an accurate center that represents the dataset. Mean is often dominated by high or low values 
(skewness) in the set, whereas the median is not affected by skewness.

Mode: the mode is the least used statistical measure, it is used when the dataset contains nominal data (i.e. gender, race, marital status, etc.).
"""

from collections import Counter 

class stats:
  def __init__(self, lenn, arr):
    self.arr = arr 
    self.arr.sort()
    self.lenn = lenn
  
  def mean(self):
      mean = sum(self.arr)/self.lenn
      return mean  

  def median(self):
      ser = self.arr
      if int(self.lenn) % 2 == 0:
          x = ser[int((int(self.lenn)/2) - 1)]
          y = ser[int(int(self.lenn)/2)]
          ret = (x+y) / 2
          return ret
      else:
          return ser[int(int(self.lenn)/2)]

  def mode(self):
      ser = self.arr
      occ = {}

      for x in ser:
        if x not in occ:
          occ[x] = 1
        else:
          occ[x] += 1
      d = [x for x, y in occ.items() if y == max(list(Counter(ser).values()))]

      if len(d) == self.lenn:
        return min(ser)
      else:
        return min(d)

strr = '6 1 1 9 1 4 7 3 5 6'

arr = [float(x) for x in str.split(strr, ' ')]
mean = stats(len(arr),arr).mean()
median = stats(len(arr),arr).median()
mode = stats(len(arr),arr).mode()

print(mean)
print(median)
print(mode)
