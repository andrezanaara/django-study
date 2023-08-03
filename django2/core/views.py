from django.shortcuts import render

from .forms import contatoForm
def index(request):
    return render(request, 'index.html')

def contato(request):
    form = contatoForm()
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')