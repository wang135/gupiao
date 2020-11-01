from django.shortcuts import render,HttpResponse

# Create your views here.


##zuixinde
import math
import json
import pandas as pd
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
#import pandas as pd
from .models import RidayProducts11
from rest_framework import serializers
import talib as ta
from django.http import HttpResponse
from rest_framework.response import Response

class PeopleinfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RidayProducts11
        fields = "__all__"

def my_view(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse("zhongyuhaol")
def ceshiaa(request):
    # hang = RidayProducts11.objects.filter(codes='000001').filter(time__gte='2019-12-01').order_by('-time').values('codes')
    # print('aaaaaaaaaaa', hang)
    #ser = PeopleinfoModelSerializer(hang, many=True)
    return HttpResponse("aaaaa")

def rihangqing(request,code):
    hang = RidayProducts11.objects.filter(codes=code).filter(time__gte='2019-12-01').order_by('-time').values('codes')
    print('aaaaaaaaaaa', hang)
    ser = PeopleinfoModelSerializer(hang, many=True)
    return Response(ser.data)
def rihangqing_day(request,code):
    hang = RidayProducts11.objects.filter(codes=code).filter(time__gte='2020-07-01').order_by('-time')
    datas = pd.DataFrame(list(hang.values()))
    #ser = PeopleinfoModelSerializer(hang, many=True)
    ret = to_json2(datas)
    # print(type(ret))
    # return HttpResponse(ret)
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")
#     #return HttpResponse("zhongyuhaollllllllllll")

def to_json2(df,orient='split'):
    df_json = df.to_json(orient = orient, force_ascii = False)
    return json.loads(df_json)
def mas(request,codes):
    ret = {}
    hang = RidayProducts11.objects.filter(codes=codes).filter(time__gte='2020-05-01').order_by('-time')
    datas = pd.DataFrame(list(hang.values()))
   # 成交量指标
    #1AD
    ad = ta.AD(datas['high'], datas['low'], datas['closes'],datas['volume'])
    ADOSC = ta.ADOSC(datas['high'], datas['low'], datas['closes'],datas['volume'], fastperiod=3, slowperiod=10)
    OBV = ta.OBV(datas['closes'],datas['volume'])
    ##动量指标
    ADX = ta.ADX(datas['high'], datas['low'], datas['closes'], timeperiod=14)
    ADXR = ta.ADXR(datas['high'], datas['low'], datas['closes'], timeperiod=14)
    AROONOSC = ta.AROONOSC(datas['high'], datas['low'], timeperiod=14)
    BOP = ta.BOP(datas['opens'], datas['high'], datas['low'], datas['closes'])
    cci = ta.CCI(datas['high'], datas['low'], datas['closes'], timeperiod=14)
    CMO = ta.CMO(datas['closes'], timeperiod=14)
    DX = ta.DX(datas['high'], datas['low'], datas['closes'], timeperiod=14)
    #MACD =
    dif, dem, histogram = ta.MACD(datas['closes'], fastperiod=12, slowperiod=26, signalperiod=9)
    #MACDEXT =
    dif, dem, histogram = ta.MACDEXT(datas['closes'], fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9,
                                  signalmatype=0)
    MFI = ta.MFI(datas['high'], datas['low'], datas['closes'],datas['volume'], timeperiod=14)
    MINUS_DI = ta.MINUS_DI(datas['high'], datas['low'], datas['closes'], timeperiod=14)
    MINUS_DM = ta.MINUS_DM(datas['high'], datas['low'], timeperiod=14)
    MOM = ta.MOM(datas['closes'], timeperiod=10)
    PLUS_DI = ta.PLUS_DI(datas['high'], datas['low'], datas['closes'], timeperiod=14)
    PPO = ta.PPO(datas['closes'], fastperiod=12, slowperiod=26, matype=0)
    ROCP = ta.ROCP(datas['closes'], timeperiod=10)
    RSI =ta.RSI(datas['closes'], timeperiod=14)
    #随机指标, 俗称KD
    slowk, slowd = ta.STOCH(datas['high'], datas['low'], datas['closes'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3,
                         slowd_matype=0)
    ##威廉指标
    WILLR = ta.WILLR(datas['high'], datas['low'], datas['closes'], timeperiod=14)


    ret = to_json2(datas)
    #print(type(ret))
    # return HttpResponse(ret)
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")


from rest_framework import serializers


# class AddForm(ModelForm):
#     class Meta:
#         model = Peopleinfo
#         fields = '__all__'
#         exclude = ['dateTime']

#