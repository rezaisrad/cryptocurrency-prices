import os, path
import requests
import pandas as pd
import time
import datetime as datetime


df = pd.DataFrame({}, columns = ['LASTUPDATE', 'HIGH24HOUR',  'LASTVOLUMETO',
                                                            'MKTCAP', 'LASTVOLUME', 'PRICE', 'SUPPLY', 'CHANGEPCT24HOUR',
                                                            'LOW24HOUR', 'OPEN24HOUR', 'VOLUME24HOURTO', 'FLAGS',
                                                            'VOLUME24HOUR', 'CHANGE24HOUR', 'TYPE', 'LASTTRADEID',
                                                            'FROMSYMBOL', 'LASTMARKET', 'MARKET', 'TOSYMBOL'])

# maximum size of API query for currency prices is 23
currency_top = ["BTC", "ETH", "XRP", "XEM", "LTC", "XLM", "ETC", "BCN", "DASH",
                            "DGB", "XMR", "SC", "DOGE", "BTS", "GNT", "ARDR", "EMC2", "ZEC",
                            "STRAT", "NXT", "STEEM", "RDD", "GNO"]
currency_str = ','.join(currency_top)
parameters  = {'fsyms': currency_str, 'tsyms': 'USD'}

while True:
    response = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
    response_json = response.json()
    currency_list = response_json['Data'].keys()
    currency_list = [currency.encode('utf8') for currency in currency_list]

    response = requests.get('https://min-api.cryptocompare.com/data/pricemultifull', params=parameters)
    crypt_dict = [response.json()['RAW'][currency]['USD'] for currency in currency_top]

    for currency in currency_top:
        crypt = response.json()['RAW'][currency]['USD']
        df = df.append(crypt, ignore_index=True)
        time.sleep(10)

    if df.size > 10000:
        df.write_csv("./data/cryptcoin_{0}.csv".format(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")))
        df = {}
