from django.shortcuts import render,redirect

from pessoa.forms import PessoaForm
from pessoa.models import Pessoa

# Create your views here.

def cadastro_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/pessoas/', kwargs={'msg':'Cadastrado com sucesso'})

    args = {
        'form':form
    }

    return render(request,'cadastro_pessoa.html',args)
    
def mostrar_pessoas(request):
    pessoas = Pessoa.objects.all()
    
    args = {
        'pessoas': pessoas
    }

    return render(request, 'mostrar_pessoas.html', args)

def updt(request, id)
    pessoas = Pessoa.objects.get(id=id)
    form = PessoasForm(request.POST or None, instance=pessoa)

      if form.is_valid():
           form.save()

        return redirect(f'../detail/{pessoas.id}')


    args = {
        'pessoas'.pessoa
        'form':form
    }

    

    return render(request, 'update.html', args)