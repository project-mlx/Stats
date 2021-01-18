"""
Calculating quartiles, minimum, maximum, and outliers
of a dataset.
"""
def ds_info(ds):
  minimum, maximum = ds[0], ds[-1]
  Q1, Q2, Q3 = None, None, None
  lower, upper = None, None
  
  length = len(ds)
  half = int(length/2)
  if length % 2 == 0: # checking if the length is divisible by 2 
    Q2 = (ds[half-1] + ds[half]) / 2 # taking the center two values to calculate the median (Q2)
    lower, upper = ds[:half], ds[half:] # extracting lower and upper split from the median 
  else:
    Q2 = ds[half] # taking the center value as the median (Q2)
    lower, upper = ds[:half], ds[half+1:] # extracting lower and upper split

  # performing the same operations as above t calculate Q1 and Q2
  sub_half = int(half/2)
  if half % 2 == 0:
    Q1 = (lower[sub_half-1] + lower[sub_half]) / 2
    Q3 = (upper[sub_half-1] + upper[sub_half]) / 2
  else:
    Q1 = lower[sub_half]
    Q3 = upper[sub_half]
  
  # calculating Interquartile range and outliers
  IQR = Q3 - Q1
  lower_boundary = Q1 - 1.5*IQR
  upper_boundary = Q3 + 1.5*IQR
  outliers = [val for val in ds if (val < lower_boundary) | (val > upper_boundary)]

  result = {'Minimum':minimum,
          'maximum':maximum, 
          'Q1':Q1,
          'Mean':'{:.1f}'.format(sum(ds)/length),
          'Median':Q2,
          'Q3':Q3,
          'IQR':IQR,
          'Outliers':outliers}

  return result

dataset = [-14, -30, -60, 6, 6, 6, 6, 6, 12, 12,
           12, 12, 8, 8, 8, 10, 10, 20, 16, 16, 16, 16, 16, 39, 58, 60]
dataset.sort()
# printing results
print(ds_info(dataset))