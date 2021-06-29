from django.urls import path

from . import views

urlpatterns = [
    #path('',views.vista,name='vista'),
    path('',views.vetApi,name='vetApi'),
    path('editar/<int:mascotasId>',views.Editar,name='editar'),
    path('agregar',views.Agregar,name='agregar'), 
    path('pet/add',views.Add,name='petAdd'),
    path('pet/delete/<int:petid>',views.delete,name='petdelete'),
    #path('dog/get',views.dogsGet,name='dogsGet'),
    #path('dog/get/<int:dogid>',views.dogsGetId,name='dogsGetId'),
    path('pet/update/<int:petid>',views.Update,name='petupdate'),
    #path('types',views.types,name='types'),
]
