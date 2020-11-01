from django.urls import path,re_path
#from .codess import views
#from .codess import views
from . import views
from django.conf.urls import url,include
code_url = [
re_path(r'(?P<code>[a-zA-Z0-9]+).html',views.rihangqing_day),
re_path(r'(?P<code>[a-zA-Z0-9]+).amma',views.rihangqing_day),
#url('uu/',views.rihangqing_day),
path('ee/',views.my_view),
   # url(r'^yunwei/$',views.mas()),
  re_path (r'(?P<codes>[a-zA-Z0-9]+)',views.mas),
#re_path(r'(?P<code>[a-zA-Z0-9]+/).html',views.rihangqing),
#url('uu/',views.rihangqing_day),
    #url(r'code/$', views.codeall.as_view()),
#url(r'aa/$', views.codes.as_view()),
    url(r'^dd/$',views.ceshiaa),
]
