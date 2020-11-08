

#API KEY：e4cae6c60e84555de2126d37fefe9537
import requests

import requests
class Fengniao:
    def __init__(self,symbol,apikey):
        self.symbol = symbol
        self.apikey = apikey
    ##历史数据
    def history(self,start_data,end_data):
        info = requests.get('https://api.trochil.cn/v1/cnstock/history',
                            params={
                                'symbol': self.symbol,
                                'start_date': start_data,
                                'end_date': end_data,
                                'apikey': self.apikey}
                            )
        print(info.text)
        return info.text
    ##最新成交价
    def quote(self):
        infos = requests.get('https://api.trochil.cn/v1/cnstock/quote',
                             params={
                                 'symbol': self.symbol,

                                 'apikey': self.apikey}
                             )
        print(infos.text)
        return infos.text

    # 日内数据
    def intraday(self,timeframe,range):
        self.timeframe = timeframe
        self.range = range


        info = requests.get('https://api.trochil.cn/v1/cnstock/intraday',
                            params={
                                'symbol': self.symbol,
                                'timeframe':  self.timeframe,
                                'range': self.range,
                                'apikey': self.apikey}
                            )
        print(info.json())
        return info.json()
