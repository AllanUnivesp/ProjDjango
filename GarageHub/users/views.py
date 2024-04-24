from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    """
    View para registro de novos usuários.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Faça login para continuar.')
            return redirect('garage:garage-home')
        else:
            # Se o formulário for inválido, exiba uma mensagem de erro
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        # Se a solicitação não for POST, inicialize um novo formulário de registro
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
