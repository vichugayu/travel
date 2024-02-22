from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, agents


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=agents.objects.all()
    return render(request,"index.html",{'result':obj,'results':obj1})

#def addition(request):
  #  x = int(request.GET['num1'])
   # y = int(request.GET['num2'])
    #res=x+y
  #  des=x*y
   # bed=x/y
   # gfd=x-y
   # return  render(request,"result.html",{'ress':res,'rem':des,'regs':bed,'gfd':gfd})
