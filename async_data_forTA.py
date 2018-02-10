import asyncio
import ccxt.async as ccxt
import pandas as pd


async def ohlcv_cex(pair):
    cex = ccxt.cex()
    while True:
        await asyncio.sleep(5)
        data = await cex.fetch_ohlcv(pair, '1m', limit=10)
        print('ohlc fetched', pair)
        df = pd.DataFrame(data, columns=('time', 'open',
                                         'hight', 'low',
                                         'close', 'volume'))
        print(df)

    return df


loop = asyncio.get_event_loop()

try:
    pair = ['ETH/EUR', 'BTC/USD', 'BTC/GBP']
    task_list = [loop.create_task(ohlcv_cex(pair[i])) for i in range(3)]
    asyncio.wait(task_list)
    loop.run_forever()

except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
