import requests
import sqlite3
import json

# Connecting to the database file
conn = sqlite3.connect('cryptcoin.db')
c = conn.cursor()

# List of columns for table
new_field = 'LASTUPDATE'
real_columns = ['HIGH24HOUR',  'LASTVOLUMETO', 'MKTCAP', 'LASTVOLUME', 'PRICE',
                            'SUPPLY', 'CHANGEPCT24HOUR', 'LOW24HOUR', 'OPEN24HOUR', 'VOLUME24HOURTO',
                            'FLAGS', 'VOLUME24HOUR', 'CHANGE24HOUR', 'TYPE', 'LASTTRADEID']
text_columns = ['FROMSYMBOL', 'LASTMARKET', 'MARKET', 'TOSYMBOL']
table_name = 'cryptocompare'   # name of the table to be created

# Adding a new column without a row value
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name, nf=new_field, ft='REAL'))

for column in real_columns:
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                        .format(tn=table_name, cn=column, ct='REAL'))
for column in text_columns:
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                    .format(tn=table_name, cn=column, ct='TEXT'))

conn.commit()
conn.close()
