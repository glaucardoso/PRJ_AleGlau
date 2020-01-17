from django.shortcuts import render

# Create your views here.

def cadastro_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/', kwargs={'msg':'Cadastrado com sucesso'})

    args = {
        'form':form
    }

    return render(request,'cadastro_pessoa.html',args)
    