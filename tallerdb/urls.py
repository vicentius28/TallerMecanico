from django.urls import path
from . import views


urlpatterns= [
    path('',views.index, name='index'),
    path('nav',views.nav,name='nav'),
    path('index',views.index,name='index'),
    path('frenos',views.frenos,name='frenos'),
    path('equipo',views.equipo,name='equipo'),
    path('otros',views.otros,name='otros'),
    path('inis',views.inis,name='inis'),
    path('regis',views.regis,name='regis')
    
]