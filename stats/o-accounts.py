eurusd = 1.068

# Waka
icm5_134_usd = 5272

# FW
icm5_120_usd = 5075

# Prado
icm5_942_eur = 2718 * eurusd

# TradeAngel
icm4_831_usd = 6500

o_accounts = [icm5_134_usd, icm5_120_usd, icm5_942_eur, icm4_831_usd]
count_accounts = 0
for acc in o_accounts:
  count_accounts += acc

print(count_accounts)

