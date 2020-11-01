"""Gupiao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from .codess import views
#from .codess import views
#from codess import views
from django.conf.urls import url,include
from codess import urls as ur
urlpatterns = [
    path('admin/', admin.site.urls),
path('code/', include(ur.code_url )),
# path(r'ee/$',views.my_view),
#    # url(r'^yunwei/$',views.mas()),
#    url(r'(?P<codes>[a-zA-Z0-9]+)',views.mas),
#     #url(r'code/$', views.codeall.as_view()),
# #url(r'aa/$', views.codes.as_view()),
#     url(r'^dd/$',views.ceshiaa),
]
