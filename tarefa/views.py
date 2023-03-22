from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import TarefaBd
from .forms import ConteudoForm
# Create your views here.

def index(request):
    conteudo = TarefaBd.objects.all()

    form=ConteudoForm()
    if request.method=='POST':
        print(request.POST)
        print("AAAAAAAAAAAAA")

        form=ConteudoForm(request.POST)
        if form.is_valid():
            form.save()
            
    context={
        'conteudos':conteudo,

        'form':form
    }
    return render(request, 'lista.html',context)