import time
from threading import Thread

from core.database.initialization import settings
from core.market.marketAPI.cryptoMarketApi import getApi

market = 'binance.com'


class MarketDataLoader(Thread):
    def __init__(self, sharedQueue, marketName):
        super().__init__(daemon=True)
        self.queue = sharedQueue
        self.marketName = marketName
        self.market = getApi(marketName)
        self.settings = [x for x in settings['markets'] if x['name'] == marketName][0]

    def run(self):
        try:
            self.requestTradeHistory()
        except Exception as e:
            print(e)
        self.requestFreshTradeData()

    def requestFreshTradeData(self):
        pass

    # Request Trade History
    # for every trade pair
    def requestTradeHistory(self):
        for tp in self.settings['tradePairs']:
            # find crypto name and currency name
            crypto, currency = tp.split('_')
            # request tradeHistory
            trades = self.market.requestTradesInfo(crypto, currency, withRowLimit=200)
            groupForTable = f"/{tp}/{self.marketName.replace('.', '')}"
            # on response put item to shared Queue
            if trades:
                item = {'group': groupForTable, 'trades': sorted(trades[tp],
                                                                 key=lambda x: x['tid'])}
                self.queue.put(item)
            else:
                print(f"Error for {groupForTable} trade request.")
            time.sleep(5)
