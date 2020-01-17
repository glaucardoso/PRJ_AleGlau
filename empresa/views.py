from django.shortcuts import render,redirect

from empresa.forms import EmpresaForm

# Create your views here.

def cadastro_empresa(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/', kwargs={'msg':'Cadastrado com sucesso'})

    args = {
        'form':form
    }

    return render(request,'cadastro_empresa.html',args)
    
 
# Create your views here.
