from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name = 'home'),
    path('todo/', views.todo, name = 'todo'),
    path('mailtodo/', views.mailtodo, name = 'mailtodo'),
    path('complete/<todo_id>', views.completeTodoToggle, name='completetoggle'),
    path('deletecomplete', views.deleteCompleted, name='deleteCompleted'),
    path('deleteall', views.deleteAll, name='deleteall'),

]