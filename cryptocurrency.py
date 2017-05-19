import os, path
import requests
import sqlite3
import json

# get list of avaiable cryptocurrencies
response = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
response_json = response.json()
currency_list = response_json['Data'].keys()
currency_list = [currency.encode('utf8') for currency in currency_list]

# maximum range of currency prices is [0:22]
currency_top = ["BTC ", "ETH", "XRP", "XEM", "LTC", "XLM", "ETC", "BCN", "DASH",
                            "DGB", "XMR", "SC", "DOGE", "BTS", "GNT", "ARDR", "EMC2", "ZEC",
                            "STRAT", "NXT", "STEEM", "RDD", "GNO"]
currency_str = ','.join(currency_top)

parameters  = {'fsyms': currency_str, 'tsyms': 'USD'}
response2 = requests.get('https://min-api.cryptocompare.com/data/pricemultifull', params=parameters)

response2.json()['RAW']['XLM']['USD'].keys()

conn = sqlite3.connect('cryptcoin.db')
cursor = conn.cursor()
cursor.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                    .format(tn=table_name, cn=new_column1, ct=column_type))

conn.commit()
conn.close()
