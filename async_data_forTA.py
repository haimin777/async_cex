# cryptocurrency data for TA in form of dataframe

import ccxt.async as ccxt
import datetime
import time
import pandas as pd
import  numpy as np
import talib
import asyncio
import os
import sys

class DataForTA:
    def __init__(self):
        self.data = []
        self.hold = 30

    def get_dataframe(self,pair, lim):
        try:

            ohlcvs = asyncio.get_event_loop().run_until_complete(ccxt.cex().fetch_ohlcv(pair, '1m', limit=lim))

           # ohlcvs = self.exchange.fetch_ohlcv('ETH/BTC', '5m', limit=lim)  # , from_timestamp, 100)
           # print(self.exchange.timeframes) #вывод доступных таймфреймов для данного рынка


            df = pd.DataFrame(np.array(ohlcvs), columns=('time', 'open',
                                                         'hight', 'low',
                                                         'close', 'volume'))

            print('data loaded OK')
            return df

        except (ccxt.ExchangeError, ccxt.AuthenticationError, ccxt.ExchangeNotAvailable, ccxt.RequestTimeout) as error:
            print('Got an error', type(error).__name__, error.args, ', retrying in', self.hold, 'seconds...')
            time.sleep(self.hold)

if __name__ == "__main__":
    d = DataForTA()
    f = d.get_dataframe(10)

    print(talib.SMA(f.close.values, 5)[-1])