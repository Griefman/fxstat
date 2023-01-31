from fxstat.stats.all_accounts import prado

prado_prc_month = [26.41, 3.57, 8.19, 11.91, 16.25, -11.83, 81.32, 66.70, -22.34, -8.11, 78.05, 19.66, -1.73, 20.32,
                   3.41, 9.63, -12.72, -13.21, 10.59, 30.19, 16.97, 19.02, 6.02, 20.19, -40.56, 26.98, -2.36, 98.23,
                   4.68, -0.24, 51.82, 21.02, -3.93, 27, -16.10, 30.48, 22.41, -15.14]

prado_avg_prc = round(sum(prado_prc_month) / len(prado_prc_month), 2)
# init_dep = 10000
deposit = 8000
# deposit_avg = 10000
count = 1
count_y = 1
for prc in prado_prc_month:
    deposit *= (1 + prc / 100)
    if count % 12 == 0:
        print(f'{count_y}-й год: {round(deposit, 2)}$')
        count_y += 1
    count += 1
print(f'На {count - 1}-й месяц: {round(deposit, 2)}$')

last_12_months = prado_prc_month[-12:]
# print(last_12_months)

flag = True

return_lst = []
for i in range(len(prado_prc_month)):
  dep = 8000

  if flag:
    end_year = i + 12
    temp_lst = prado_prc_month[i:end_year]
    if len(temp_lst) < 12:
      flag = False
    else:
      for month in temp_lst:
        dep *= (1 + month / 100)
      return_lst.append(int(dep))
counter = 0
for dep in return_lst:
  counter += dep

avg_year_return = counter / len(return_lst)
print(f'Среднегодовой возврат: {int(avg_year_return)} $')
print(f'Минимальный возврат: {int(min(return_lst))} $')
print(f'Максимальный возврат: {int(max(return_lst))} $')

