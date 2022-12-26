
percents = [29.35, 12.53, 35.89, 27.28]
deposit = 10000

for percent in percents:
  deposit *= 1 + percent / 100

print(deposit)
