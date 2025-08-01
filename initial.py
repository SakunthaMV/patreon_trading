def access_bybit_profile():
    return HTTP(
        testnet=False,
        api_key="jbZNqIEuoC64EbGHZR",
        api_secret="gJqIqk6F6DNGqokiDZcED5dAILO7aqIuC1ur",
    )

def get_balance():
    try:
        session = access_bybit_profile()
        resp = session.get_wallet_balance(accountType="UNIFIED",coin="USDT")["result"]["list"][0]["coin"][0]["walletBalance"]
        return resp
    except Exception as err:
        print(err)

print(get_balance())
