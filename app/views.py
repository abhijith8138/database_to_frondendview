from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic (request):
    LOT=Topic.objects.all()
    d={'topic': LOT}
    return render(request,'display_topic.html',context=d)
def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'web':LOW}
    return render(request,'display_webpage.html',context=d)
def display_accessrecord(request):
    LOA=Accessrecord.objects.all()
    d={'access':LOA}
    return  render(request,'display_accessrecord.html',context=d)