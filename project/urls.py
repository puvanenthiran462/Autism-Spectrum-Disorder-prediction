
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('asd/',views.asd,name='asd'),
    path('result/',views.result,name="result"),
    path('spectrum/',views.spectrum,name="spectrum")
   

   
]
