eurusd = 1.051
usdchf = 0.938
btc = 16925

# Waka + FW + Fringe
icm5_685_chf = 10811 / usdchf

# Prado
robo4_233_btc = 0.233 * btc
robo4_297_usd = 3268
jappu4_306 = 436
# TradeAngel
icm4_451_usd = 7242
robo4_612_eur = 6562 * eurusd

# WolfScalper
rann5_353_usdt = 901

# Signal + WolfScalper
icm5_679_usd = 1103

# Other
robo4_109_usd = 408
aafx5_665 = 250

all_accounts = [icm5_685_chf, robo4_233_btc, robo4_297_usd, jappu4_306, icm4_451_usd, robo4_612_eur, rann5_353_usdt,
                icm5_679_usd, robo4_109_usd, aafx5_665]

robo_accounts = sum([robo4_233_btc, robo4_297_usd, robo4_612_eur, robo4_109_usd])
icm_accounts = sum([icm5_685_chf, icm4_451_usd, icm5_679_usd])

count_accounts = 0
for acc in all_accounts:
  count_accounts += acc

print(f'Сумма всех счетов: {round(count_accounts, 2)} $')
print(f'Roboforex: {round(robo_accounts, 2)}')
print(f'IC Markets: {round(icm_accounts, 2)}')

