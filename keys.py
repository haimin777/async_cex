import  asyncio
import ccxt.async as ccxt

class CexKey:
    def __init__(self):
        self.cex = ccxt.cex({
            'apiKey': "Api key",
            'secret': "Secret api key",
            'uid': 'your ID',
            'verbose': False,
        })