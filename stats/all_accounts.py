eurusd = 1.0868
usdchf = 0.92
btc = 23386

# Waka + FW + Fringe
icm5_685_chf = 11713 / usdchf

# Prado
robo4_233_btc = 0.227 * btc
robo4_297_usd = 2470
jappu4_306 = 308
prado = robo4_233_btc + robo4_297_usd + jappu4_306
print(f'Prado: {int(prado)} $')
# TradeAngel
icm4_451_usd = 6540
robo4_612_eur = 6200 * eurusd

# Among Us
rann5_353_usdt = 1041

# Apex Trader
icm5_679_usd = 959

# Other
robo4_109_usd = 408
aafx5_665 = 263

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

