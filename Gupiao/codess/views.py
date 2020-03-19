from django.shortcuts import render,HttpResponse

# Create your views here.


import pandas as pd
from .models import Dayhangqing1
def mas(request,codes):
    hang = Dayhangqing1.objects.filter(codes=codes).filter(time__gte='2019-12-01').order_by('-time')
    datas = pd.DataFrame(list(hang.values()))

    print(datas)
    return HttpResponse(datas)


