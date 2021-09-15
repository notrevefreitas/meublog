from django.urls import path
from django.urls.resolvers import URLPattern 
from .import views 



urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:pk>/',views.detalhe_postagem,name='detalhe_postagem'),
    path('edit_postagem/<int:pk>/',views.edit_postagem,name="edicao_postagem"),
    path('post/new/',views.adicionar_postagem,name='adicionar_postagem')
    ]