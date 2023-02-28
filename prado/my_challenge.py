# На 1-ое Марта 2023
start_robo_btc = 204.53
start_robo_usd = 2197
start_icm_usd = 8828
start_alpari_usd = 498
start_course_btc = 23306
# 15791$
start_deposit = start_robo_btc * start_course_btc / 1000 + start_robo_usd + start_icm_usd +\
                start_alpari_usd
print(start_deposit)
# ----
current_robo_btc = 204.53
current_robo_usd = 2197
current_icm_usd = 8828
current_alpari_usd = 498
current_course_btc = 23306

current_deposit = current_robo_btc * current_course_btc / 1000 + current_robo_usd + current_icm_usd +\
                  current_alpari_usd

print(current_deposit)
