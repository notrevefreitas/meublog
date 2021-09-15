from django.shortcuts import redirect ,get_object_or_404, render
from blog.models import Postagem
from .forms import PostForms 
from django.utils import timezone


# Create your views here.

def home(request):
    postagens = Postagem.objects.all().order_by("-data_criacao")
    return render(request,'home.html',{'postagens': postagens})

def detalhe_postagem(request,pk):
    postagem = Postagem.objects.get(pk=pk)
    return render(request,'detalhe_postagem.html',{'postagem':postagem})

def adicionar_postagem(request):
    if request.method == "POST":
        #Quando for para salvar 
        form =PostForms(request.POST)
        if form.is_valid():
            postagem= form.save(commit=False)
            postagem.autor = request.user
            postagem.data_publicacao = timezone.now()
            postagem.save()
            return redirect('home')
    else:
        #primeiro acesso 
        form = PostForms()
    return render(request,'editar_postagem.html',{'form':form})

def edit_postagem(request,pk):
    postagem = get_object_or_404(Postagem, pk=pk)
    if request.method == "POST":
        #Quando for para salvar 
        form =PostForms(request.POST,instance=postagem)
        if form.is_valid():
            postagem= form.save(commit=False)
            postagem.autor = request.user
            postagem.data_publicacao = timezone.now()
            postagem.save()
            return redirect('home')
    else:
        #primeiro acesso 
        form = PostForms(instance=postagem)
    return render(request,'editar_postagem.html',{'form':form})
