initial_deposit = 5000
x = 0.1425

for i in range(12):
  n = initial_deposit // 5000
  k =  n * x
  print(k)
  initial_deposit += n * 5000 * k

  print(initial_deposit)
