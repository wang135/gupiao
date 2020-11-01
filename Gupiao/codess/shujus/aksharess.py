

import akshare as ak
class Xshare:
    def __init__(self,code):
        self.code = code


    ##上海证券交易所-股票数据总貌
    def stock_sse_summary(self):
        stock_sse_summary_df = ak.stock_sse_summary()
        return stock_sse_summary_df


    ##深圳证券交易所-市场总貌
    def stock_szse_summary(self):
        stock_szse_summary_df = ak.stock_szse_summary(date="20200619")
        print(stock_szse_summary_df)
        return stock_szse_summary_df
    ##A 股上市公司的实时行情数据
    def stock_zh_a_spot(self):
        stock_zh_a_spot_df = ak.stock_zh_a_spot()
        return stock_zh_a_spot_df

    ##股票数据复权
    def stock_zh_a_daily(self):
        stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol="sh600582", adjust="hfq")
        return stock_zh_a_daily_hfq_df

    ## 分时数据
    def stock_zh_a_minute(self):
        stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol='sh600751', period='1', adjust="qfq")
        return stock_zh_a_minute_df
    ##
    ##某个A上市公司的近5个交易日的历史分笔行情数据
    def stock_zh_a_tick_163(self):
        stock_zh_a_tick_163_df = ak.stock_zh_a_tick_163(code="sh600848", trade_date="20200408")
        print(stock_zh_a_tick_163_df)
        return stock_zh_a_tick_163_df

    ##指数行情
    def stock_zh_index_spot(self):
        stock_df = ak.stock_zh_index_spot()
        return stock_df

    ## 获取股票指数(或者股票)历史行情数据
    def stock_zh_index_daily_tx(self):
        stock_zh_index_daily_tx_df = ak.stock_zh_index_daily_tx(symbol="sh000919")
        return stock_zh_index_daily_tx_df
    ## 科创部
    def stock_zh_kcb_spot(self):
        stock_zh_kcb_spot_df = ak.stock_zh_kcb_spot()
        return stock_zh_kcb_spot_df

    ##股权质押市场概况
    def stock_em_gpzy_profile(self):
        stock_em_gpzy_profile_df = ak.stock_em_gpzy_profile()
        return stock_em_gpzy_profile_df

    ##股权质押-上市公司质押比例
    def stock_em_gpzy_pledge_ratio(self):
        stock_em_gpzy_pledge_ratio_df = ak.stock_em_gpzy_pledge_ratio(trade_date="2020-08-14")
        return stock_em_gpzy_pledge_ratio_df
    ##股权质押-重要股东股权质押明细
    def stock_em_gpzy_pledge_ratio_detail(self):
        stock_em_gpzy_pledge_ratio_detail_df = ak.stock_em_gpzy_pledge_ratio_detail()
        return stock_em_gpzy_pledge_ratio_detail_df

    ##东方财富分析师指数2020最新排行

    def stock_em_analyst_rank(self):
        stock_em_analyst_rank_df = ak.stock_em_analyst_rank()
        return stock_em_analyst_rank_df

    ##千股千评
    def stock_em_comment(self):
        stock_em_comment_df = ak.stock_em_comment()
        return stock_em_comment_df