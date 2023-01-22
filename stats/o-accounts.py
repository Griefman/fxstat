eurusd = 1.08

# Waka
icm5_134_usd = 5200

# FW
icm5_120_usd = 5403

# Prado
icm5_942_eur = 2864 * eurusd

# TradeAngel
icm4_831_usd = 6171

o_accounts = [icm5_134_usd, icm5_120_usd, icm5_942_eur, icm4_831_usd]
count_accounts = 0
for acc in o_accounts:
  count_accounts += acc

print(count_accounts)
# Недельные данные на 22.01.2023
weeks = [19749, 19867]
