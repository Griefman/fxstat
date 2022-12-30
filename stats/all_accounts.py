eurusd = 1.068
usdchf = 0.925
btc = 16525

# Waka + FW + Fringe
icm5_685_chf = 10811 / usdchf

# Prado
robo4_233 = 0.228 * btc
robo4_297 = 3180
jappu4_306 = 413
# TradeAngel
icm4_451_usd = 7036
robo4_612_eur = 6463 * eurusd

# WolfScalper
rann5_353_usdt = 901

# Signal + WolfScalper
icm5_679_usd = 1103

# Other
robo4_109 = 408
aafx5_665 = 250

all_accounts = [icm5_685_chf, robo4_233, robo4_297, jappu4_306, icm4_451_usd, robo4_612_eur, rann5_353_usdt,
                icm5_679_usd, robo4_109, aafx5_665]

count_accounts = 0
for acc in all_accounts:
  count_accounts += acc

print(count_accounts)
