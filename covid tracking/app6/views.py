from django.shortcuts import render
from covid import Covid

def showIndex(request):
    covid = Covid()
    covid_info = covid.get_data()
    return render(request,"index.html",{'data':covid_info})