from django.shortcuts import render

from django.http import HttpResponse
def index(request):
     return render(request,"polls/home.html")


def contact(request):
            return render(request,"polls/basic.html",{'contact':['If you want to contant me, Email me.','  tkhandagre910@gmail.com']})
