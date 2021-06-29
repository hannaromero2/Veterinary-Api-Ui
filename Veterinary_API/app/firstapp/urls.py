from django.urls import path

from . import views

urlpatterns = [
    path('',views.vista,name='vista'),
    path('servicios',views.servicios,name='servicios'),
    path('pet',views.pet,name='pet'),
    path('owner',views.owner,name='owner'),
    path('pet/add',views.petAdd,name='petAdd'),
    path('pet/delete',views.petDelete,name='petdelete'),
    path('pet/search/<int:petid>',views.petGet,name='petget'),
    path('pet/update/<int:petid>',views.update,name='petget'),
]
