from threading import Thread

from core.market.marketAPI import cryptoMarketApi


class TradesRequester(Thread):
    def __init__(self, withResponseQueue, withMarketURL):
        super().__init__(daemon=True)
        self.queue = withResponseQueue
        self.url = withMarketURL

    def run(self):
        marketAPI = cryptoMarketApi.getApi(self.url)[0]
        while True:
            try:
                self.requestTradesFrom(marketAPI)
            except Exception as err:
                print(err)
            time.sleep(delayForRequests)

    def requestTradesFrom(self, marketAPI):
        isFirstTime = True
        for crypto in cryptoCoins:
            for currency in currencyCoins:
                if isFirstTime:
                    trades = marketAPI.requestTradesInfo(crypto, currency, withRowLimit=None)
                else:
                    trades = marketAPI.requestTradesInfo(crypto, currency, withRowLimit=200)
                tradePair = f"{crypto}_{currency}"
                groupForTable = f"/{tradePair}/{self.url.replace('.', '')}"
                if trades:
                    item = {'group': groupForTable, 'trades': sorted(trades[tradePair],
                                                                     key=lambda x: x['tid'])}
                    self.queue.put(item)
                else:
                    print(f"Error for {groupForTable} trade request.")
                time.sleep(5)
