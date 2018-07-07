import requests
import time
import serial

def get_dif(first, now):
    dif = now-first
    percentage = (dif/now)*100
    return percentage

def get_price(coin_name):
    resp = requests.get(url="https://api.bitso.com/v3/ticker/?book="+coin_name)
    if resp.status_code == 200:
        coin = resp.json()
        if coin['success'] == True:
            price = coin['payload']['last']
            return price


try:
    btc_dif = 0
    eth_dif = 0
    trigger = 0
    while True:
        print(trigger)
        if trigger == 0:
            btc_mxn_first = get_price("btc_mxn")
            eth_mxn_first = get_price("eth_mxn")
        trigger = trigger+1
        btc_mxn_now = get_price("btc_mxn")
        eth_mxn_now = get_price("eth_mxn")
        if trigger == 2:
            btc_dif = get_dif(float(btc_mxn_first), float(btc_mxn_now))
            eth_dif = get_dif(float(eth_mxn_first), float(eth_mxn_now))
            trigger = 0
        print(btc_mxn_now)
        print(eth_mxn_now)
        print(eth_dif)
        print(btc_dif)
        time.sleep(30)

except KeyboardInterrupt:
    print("Succes: False")
