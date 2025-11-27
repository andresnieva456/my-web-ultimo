from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('desayunos/', views.desayunos, name='desayunos'),
    path('almuerzos/', views.almuerzos, name='almuerzos'),
    path('cenas/', views.cenas, name='cenas'),
]
