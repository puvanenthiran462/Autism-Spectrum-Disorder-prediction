from django.shortcuts import render
from django.http import HttpResponse
# Create your models here.
from django.db import models


import joblib
import os


# Create your views here.

def index(request):
    return render(request,"index.html")

def asd(request):
    return render(request,"asd.html")



def result(request):
    
    
    cls = joblib.load('ml_model/logistic_regression_model.joblib')

    lis=[]
    re=0
    if request.method == 'POST':
            lis.append(int(request.POST['A1_Score']))
            lis.append(int(request.POST['A2_Score']))
            lis.append(int(request.POST['A3_Score']))
            lis.append(int(request.POST['A4_Score']))
            lis.append(int(request.POST['A5_Score']))
            lis.append(int(request.POST['A6_Score']))
            lis.append(int(request.POST['A7_Score']))
            lis.append(int(request.POST['A8_Score']))
            lis.append(int(request.POST['A9_Score']))
            lis.append(int(request.POST['A10_Score']))


            
                 

            lis.append(int(request.POST['age']))
            
            if request.POST['gender'] == 'male':
                 lis.append(1)
            else:
                 lis.append(0)
        
            if request.POST['jundice'] == 'yes':
                 lis.append(1)
            else:
                 lis.append(0)
            if request.POST['autism'] == 'yes':
                 lis.append(1)
            else:
                 lis.append(0)
            lis.append(0)
            for i in range(0,10):
                 re+=lis[i]
            lis.append(re)
        

    ans = cls.predict([lis])    
      
    
    return render(request,"result.html",{"list":ans})
            
    



def spectrum(request):
    return render(request,"spectrum.html")

