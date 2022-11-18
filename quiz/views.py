from .forms import CreateUserForm, NovaPergunta
from .models import Categoria, Pergunta
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view


@api_view()
def index(request):
    if request.user.is_authenticated:
        lista_de_categorias = Categoria.objects.all()
        contexto = {'lista_de_categorias': lista_de_categorias}
        return render(request, 'quiz/index.html', contexto)
    else:
        return redirect('entrar')


@api_view(['GET', 'POST'])
def categoria(request, categoria: int):
    if not request.user.is_authenticated:
        return redirect('entrar')
    else:
        if request.method == 'POST':
            print(request.POST)
            perguntas = Pergunta.objects.filter(categoria=categoria)
            pontos = 0
            errado = 0
            correto = 0
            total = 0
            for p in perguntas:
                total += 1
                resposta = request.POST.get(p.pergunta)
                items = vars(p)
                print(items[resposta])
                if p.resposta == items[resposta]:
                    pontos += 1
                    correto += 1
                else:
                    if pontos > 0:
                        pontos -= 1
                    else:
                        pontos = 0
                    errado += 1
            percentagem = pontos / (total * 1) * 100
            contexto = {
                'pontos': pontos,
                'tempo': request.POST.get('timer'),
                'correto': correto,
                'errado': errado,
                'percentagem': percentagem,
                'total': total,
            }
            return render(request, 'quiz/resultado.html', contexto)
        else:
            perguntas = Pergunta.objects.all()
            contexto = {'perguntas': perguntas}
            return render(request, 'quiz/categoria.html', contexto)


@api_view(['GET', 'POST'])
def nova_pergunta(request):
    if request.user.is_staff:
        form = NovaPergunta()
        if request.method == 'POST':
            form = NovaPergunta(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        contexto = {'form': form}
        return render(request, 'quiz/nova_pergunta.html', contexto)
    else:
        return redirect('index')


@api_view(['GET', 'POST'])
def registro(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('entrar')
        contexto = {
            'form': form,
        }
        return render(request, 'quiz/registro.html', contexto)


@api_view(['GET', 'POST'])
def entrar(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        contexto = {}
        return render(request, 'quiz/entrar.html', contexto)


@api_view()
def sair(request):
    logout(request)
    return redirect('/')
