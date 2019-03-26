import urllib3
import json
import time
from datetime import datetime

http = urllib3.PoolManager()
urllib3.disable_warnings()


class PriceCrawer:
    """"""

    def __init__(self, country: int = 37,
                 currency: int = 1,
                 payMethod: int = 0,
                 currPage: int = 1,
                 coinId: int = 1,
                 tradeType: str = 'buy',
                 blockType: str = 'general',
                 online: int = 1):
        """

        :param country: default 37 for China
        :param currency: default 1 for CNY
        :param payMethod: does not matter
        :param currPage: default 1 for the information at the first page
        :param coinId: default 1 for BitCoin(for different purpose with other type of crypto)
        3 for ETH and so on .......
        :param tradeType: does not matter
        :param blockType: does not matter
        :param online: web tech, does not matter
        """
        self.country = country
        self.currency = currency
        self.payMethod = payMethod
        self.currPage = currPage
        self.coinId = coinId
        self.tradeType = tradeType
        self.blockType = blockType
        self.online = online

    def fetch_data(self):
        self.url = 'https://otc-api.eiijo.cn/v1/data/trade-market?' + \
                   'country=' + \
                   str(self.country) + \
                   '&currency=' + \
                   str(self.currency) + \
                   '&payMethod=' + \
                   str(self.payMethod) + \
                   '&currPage=' + \
                   str(self.currPage) + \
                   '&coinId=' + \
                   str(self.coinId) + \
                   '&tradeType=' + \
                   str(self.tradeType) + \
                   '&blockType=' + \
                   str(self.blockType) + \
                   '&online=' + \
                   str(self.online)

        self.market_feed = http.request('GET', self.url)

        self.string_data = self.market_feed.data.decode()

    def show_data(self):
        self.market_data = json.loads(self.string_data)
        for i in range(4):
            print(datetime.now())
            print('pirce_' + str(i), '---', self.market_data['data'][i]['price'])


bitcoin_crawer = PriceCrawer(coinId=1)
while True:
    bitcoin_crawer.fetch_data()
    bitcoin_crawer.show_data()
    time.sleep(3)
