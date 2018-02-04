import talib
import ccxt
from async_data_forTA import DataForTA
from async_account_ccxt import AccountInfo

class Algorithm:
    def __init__(self):
        self.data_ta = DataForTA().get_dataframe('ETH/EUR', 40)


    def sma_cross(self):
        sma_short = talib.SMA(self.data_ta.close.values, 5)[-1]
        sma_long = talib.SMA(self.data_ta.close.values, 35)[-1]
        allow = sma_short > sma_long
        print(sma_long, sma_short)
        return allow

    def start(self, AccountInfo):
        #выводим доступный балланс
        print(AccountInfo.balance())


#расчитаем две SMA
if __name__ == "__main__":
    '''
    d = DataForTA()
    data_ta = d.get_dataframe('ETH/USD', 60)
    sma_short = talib.SMA(data_ta.close.values, 5)[-1]
    sma_long = talib.SMA(data_ta.close.values, 35)[-1]
    print('sma_short = ', sma_short, 'sma_long = ', sma_long)
    '''
    a = Algorithm()
    a.start(AccountInfo('USD'))
    print(a.sma_cross())