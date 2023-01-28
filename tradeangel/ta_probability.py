import numpy as np
deposit = 6000
lot_size = 1
lot_increase_factor = 2
max_lot_size = 16
trades = 2000
# Функция вазвращает случайные 0 или 1, где р - вероятность выпадения 1 (в данном случае)


def coin_flip(p):
    result = np.random.binomial(1, p)
    return result


current_lot = lot_size

negative_deposits = []
for i in range(trades):
    value_trade = coin_flip(0.53)
    print_lot = current_lot
    if value_trade == 1:
        deposit += 40 * current_lot
        current_lot = lot_size
    else:
        deposit -= 45 * current_lot
        current_lot = lot_increase_factor * current_lot

    if deposit < 5000:
        lot_size = 1
        max_lot_size = lot_size * 16
    else:
        lot_size = deposit // 5000
        max_lot_size = lot_size * 16
        if current_lot > max_lot_size:
            current_lot = lot_size

    if deposit < 0:
        negative_deposits.append(deposit)
    print(value_trade, print_lot, lot_size, max_lot_size, deposit)
# print(deposit)
if negative_deposits:
    print(min(negative_deposits))
