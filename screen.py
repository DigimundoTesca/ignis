import requests
import time
import serial

def get_price(coin_name):
    resp = requests.get(url="https://api.bitso.com/v3/ticker/?book="+coin_name)
    if resp.status_code == 200:
        coin = resp.json()
        if coin['success'] == True:
            price = coin['payload']['last']
            return price


try:
    trigger = 0
    while True:
        if trigger == 0:
           btc_mxn_last = get_price("btc_mxn")
           eth_mxn_last = get_price("eth_mxn")
           print(btc_mxn_last)
           print(eth_mxn_last)
           time.sleep(30)
        else:
            btc_mxn_now = get_price("btc_mxn")
            eth_mxn_now = get_price("eth_mxn")

except KeyboardInterrupt:
    print("Succes: False")
