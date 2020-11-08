

from jqdatasdk import *
auth('18604309462', '18604309462wangJ')
# 查询是否连接成功
is_auth = is_auth()
print(is_auth)

 #获取所有沪深300的股票, 设为股票池
stocks = get_index_stocks('000300.XSHG')
class Jukuan:
    def __init__(self,name,keys):
        self.name =name
        self.keys = keys
    # def auth(self):
    #     auth(self.name, self.keys)
    #     # 查询是否连接成功
    #     is_auth = is_auth()
    #     print(is_auth)

    # 日行情
    def days(self,code,start_date,end_date,frequency):
        auth(self.name, self.keys)
        df = get_price(code, start_date=start_date, end_date=end_date, frequency=frequency)
        return df

    # 分钟行情
    def fenzhong(self):
        auth(self.name, self.keys)
        df = get_price('000001.XSHE', start_date='2015-12-01 14:00:00', end_date='2015-12-02 12:00:00', frequency='1m')
        return df
    ##融资融券
    def rongzi(self,code_list,start_date,end_date):
        auth(self.name, self.keys)
        df = get_mtss(['000001.XSHE', '000002.XSHE', '000099.XSHE'], start_date, end_date)
        return df
    ##
    ##获取指数成份股
    def zjishu(self,index_symbol,date):
        auth(self.name, self.keys)
        df = get_index_stocks(index_symbol, date=date)
        return df

    ##获取行业的股票
    def industry(self,industry_code,date):
        auth(self.name, self.keys)
        df = get_industry_stocks(industry_code, date=date)
        return df

##获取概念股的成分股
    def gainian(self,gainian_code,date):
        auth(self.name, self.keys)
        df = get_concept_stocks(gainian_code, date=date)
        return df

    # 查询股票所属行业
    def chahangye(self,code):
        auth(self.name, self.keys)
        df = get_industry(code, date=None)
        return df


#df = get_concept_stocks('GN1097', date=None)



#
# # 获取一支股票
# df = get_price('000001.XSHE') # 获取000001.XSHE的2015年的按天数据
# df = get_price('000001.XSHE', start_date='2015-01-01', end_date='2015-02-01', frequency='daily', fields=['open', 'close']) # 获得000001.XSHE的2015年01月的日线数据, 只获取open+close字段
# df = get_price('000001.XSHE', start_date='2015-12-01 14:00:00', end_date='2015-12-02 12:00:00', frequency='1m') # 获得000001.XSHE的2015年12月1号14:00-2015年12月2日12:00的分钟数据
#
# # 获取多只股票
# panel =  get_price(get_index_stocks('000903.XSHG')) # 获取中证100的所有成分股的2015年的天数据, 返回一个[pandas.Panel]
# df_open = panel['open']  # 获取开盘价的[pandas.DataFrame],  行索引是[datetime.datetime]对象, 列索引是股票代号
# df_volume = panel['volume']  # 获取交易量的[pandas.DataFrame]
# df_open['000001.XSHE'] # 获取平安银行的2015年每天的开盘价数据
#
# # 获取多只股票的融资融券信息
# get_mtss(['000001.XSHE', '000002.XSHE', '000099.XSHE'], '2015-03-25', '2016-01-25')
#
# ##获取指数成份股
# df = get_index_stocks(index_symbol, date=None)
#
# ##获取行业的股票
# get_industry_stocks(industry_code, date=None)
# ##获取概念股的成分股
# df = get_concept_stocks('GN1097', date=None)
#
# ##
# #  get_industries 获取行业列表
# # get_concepts 获取概念列表
#
#
# #查询股票所属行业
#
# get_industry(security, date=None)
