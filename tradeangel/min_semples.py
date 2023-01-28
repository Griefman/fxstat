import numpy as np

def coin_flip(p):
  result = np.random.binomial(1, p)
  return result

count_0 = 0
count_1 = 0

for i in range(10000):
  semple = coin_flip(0.5)
  if semple == 0:
    count_0 += 1
  else:
    count_1 += 1

percent_0 = count_0 / (count_0 + count_1)
percent_1 = count_1 / (count_0 + count_1)


print(f'{round(percent_0, 5)} %')
print(f'{round(percent_1, 5)} %')
