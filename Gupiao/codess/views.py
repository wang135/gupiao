from django.shortcuts import render,HttpResponse

# Create your views here.

import json
import pandas as pd
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
import pandas as pd
from .models import Dayhangqing1

def mas(request,codes):
    ret = {}
    hang = Dayhangqing1.objects.filter(codes=codes).filter(time__gte='2019-12-01').order_by('-time')
    datas = pd.DataFrame(list(hang.values()))

    print(datas)
    ret['open'] = list(datas['opens'])
    # return HttpResponse(datas)
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")


from rest_framework import serializers


# class AddForm(ModelForm):
#     class Meta:
#         model = Peopleinfo
#         fields = '__all__'
#         exclude = ['dateTime']

class PeopleinfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dayhangqing1
        fields = "__all__"
class codeall(APIView):
    def get(self,request):
        hang = Dayhangqing1.objects.filter(codes='000001').filter(time__gte='2019-12-01').order_by('-time')
        ser = PeopleinfoModelSerializer(instance=hang,many=True)
        ret = json.dumps(ser,ensure_ascii=False)
        return HttpResponse(ret)
