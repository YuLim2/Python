import pyupbit

access = "yaHMr3mlz5RskJtx6WheyoKQui5o6a22IbiEwLmB"          # 본인 값으로 변경
secret = "sS8k1oxtOMS0GgPrnPdyXgjKcGxDNOZnqGpqoa4o"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회