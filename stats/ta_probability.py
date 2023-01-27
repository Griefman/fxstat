import numpy as np
deposit = 5000
lot_size = 1
lot_increase_factor = 2
max_lot_size = 16
trades = 800
# Функция вазвращает случайн  ые 0 или 1, где р - вероятность выпадения 1 (в данном случае)


def coin_flip(p):
    result = np.random.binomial(1, p)
    return result


current_lot = lot_size

negative_deposits = []
for i in range(trades):
    value_trade = coin_flip(0.55)
    if value_trade == 1:
        deposit += (50 * current_lot) * 0.9
        current_lot = lot_size
        if deposit > 5000:
            lot_size = deposit // 5000
            max_lot_size = lot_size * 16
    else:
        deposit -= (50 * current_lot) * 0.9
        current_lot = lot_increase_factor * current_lot
        if current_lot > max_lot_size:
            current_lot = lot_size
    if deposit < 0:
        negative_deposits.append(deposit)

print(deposit)
if negative_deposits:
    print(min(negative_deposits))
