import requests
def shenwan(df,dicts_two_zjh):
    a =-99
    for k in dicts_two_zjh:
        if df['code'] in dicts_two_zjh[k]:
            a =k
    return a
from bs4 import BeautifulSoup
import json
import time
import pandas as pd
import tushare as ts
class Xinlang:
    def __init__(self,url):
        self.url = url
    def base(self):

        #url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodes'
        url = self.url
        html = requests.get(url=url)
        aa = json.loads(html.text)
        print(aa)

        bb = aa[1][0][1]
        return bb
    ## 新浪行业0，申万行业1，热门概念3，概念板块4，地域板块5
    def xl_industry(self,num):
        bb = self.base()

        dicts_pd = {}
        shenwan = bb[num][1]
        for uu in shenwan:
            list_name = []
            name = uu[0]
            #print("aaa", name)
            wz = uu[2]
            for num in range(0, 11):
                nums = str(num)
                time.sleep(3)

                # url_1 = "http://vip.stock.finance.sina.com.cn/mkt/#sw_jxsb"
                # url_1 = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=80&sort=symbol&asc=1&node=sw_jxsb&symbol=&_s_r_a=init"
                url_1 = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=" + nums + "&num=80&sort=symbol&asc=1&node=" + wz + "&symbol=&_s_r_a=init"
                html_1 = requests.get(url=url_1)
                yy = html_1.text
                if yy != '[]':
                    # if yy !=[]:
                    # print(len(yy))
                    aa = json.loads(yy)
                    for bbb in aa:
                        code = bbb['code']
                        # print(code)
                        list_name.append(code)
            dicts_pd[name] = list_name
        dfa = pd.DataFrame([dicts_pd])
        dfa1 = dfa.T
        dfa1.columns = ['list_name']
        index_list = list(dfa1.index)

        columns_list = list(dfa1['list_name'])
        dict_name = dict(zip(index_list, columns_list))
        return dict_name
    ## 申万2级2,证监会6
    def shju_deep(self,num):
        bb = self.base()
        result_lisan = []
        df_all2 = pd.DataFrame()
        df_all = pd.DataFrame([{'yiji_name': 0, "erji_name": 0, "list_name": 0}])
        listall = []
        shenwan_two = bb[num][1]
        for uu in shenwan_two:
            print(uu)
            dicts_pd1 = {}
            yiji_name = uu[0]
            dicts_pd1['yiji_name'] = yiji_name
            for tt in uu[1]:
                print(tt)

                list_name = []
                erji_name = tt[0]
                dicts_pd1['erji_name'] = erji_name
                wz = tt[2]
                for num in range(0, 3):
                    nums = str(num)
                    time.sleep(3)

                    # url_1 = "http://vip.stock.finance.sina.com.cn/mkt/#sw_jxsb"
                    # url_1 = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=80&sort=symbol&asc=1&node=sw_jxsb&symbol=&_s_r_a=init"
                    url_1 = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=" + nums + "&num=80&sort=symbol&asc=1&node=" + wz + "&symbol=&_s_r_a=init"
                    html_1 = requests.get(url=url_1)
                    yy = html_1.text
                    if yy != '[]':
                        # if yy !=[]:
                        # print(len(yy))
                        aa = json.loads(yy)
                        for bbb in aa:
                            code = bbb['code']
                            # print(code)
                            list_name.append(code)
                dicts_pd1['list_name'] = list_name
                df1 = pd.DataFrame([dicts_pd1])
                result_lisan.append(df1)
        result_pd = pd.concat(result_lisan, ignore_index=True)
        #print(result_pd)
        return result_pd


    ## 输出code 的lable
    def hebing(self,num):
        xl_industry = self.xl_industry(num)
        stock_base = ts.get_today_all()
        stock_code = stock_base[['code', 'name']]
        stock_code['securities_deep'] = stock_code.apply(lambda x: shenwan(x,xl_industry), axis=1)
        return stock_code
if __name__ == "__main__":
    list_all =[]
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodes'
    gha = Xinlang(url)
    #新浪行业0，申万行业1，热门概念3，概念板块4，地域板块5
    for i in [0,1,3,4,5]:
        ff = gha.hebing(i)
        list_all.append(ff)
        print(ff)