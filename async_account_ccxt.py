# -*- coding: utf-8 -*-

import os
import sys
import asyncio
import ccxt.async as ccxt  # noqa: E402
from keys import CexKey

class AccountInfo:
    def __init__(self, CexKey):

        self.keys = CexKey()
        self.cex = self.keys.cex


    def balance(self, currency):

        b = asyncio.get_event_loop().run_until_complete(self.cex.fetch_balance())
        return  b[currency]['free']

    def orders(self):
        ord = asyncio.get_event_loop().run_until_complete(self.cex.fetch_open_orders())
        return ord
        
    def positions(self):

        pos = asyncio.get_event_loop().run_until_complete(self.cex.fetch_total_balance())
        print('Open positions: ')
        for key in pos:
            if pos[key] !=0:
                print(key, pos[key])
        return pos



if __name__ == '__main__':

    dd = AccountInfo(CexKey)
    print(dd.balance('USD'))
    print(dd.orders())
    #print(dd.positions())
    dd.positions()
