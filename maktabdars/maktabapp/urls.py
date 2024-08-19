from django.urls import path
from .views import home, talaba, baho, fan, fanadd, bahoadd, oquvchiadd

urlpatterns = [
    path('',home,name='home'),
    path('royxat/',talaba,name='royxat'),
    path('baho/',baho,name='baholar'),
    path('fan/',fan,name='fanlar'),
    path('addfanlar/',fanadd,name='fanlaradd'),
    path('addbaholar/',bahoadd,name='baholaradd'),
    path('addtalablar/',oquvchiadd,name='oquvchilaradd'),

]
