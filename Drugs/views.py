from django.shortcuts import render
from . models import Newdrug
# Create your views here.

def index(request):
    return render(request,"Drugs/index.html",{
        "Newdrug":Newdrug.objects.all()
    })
