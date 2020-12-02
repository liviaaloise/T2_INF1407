from django.urls.conf import path
from todoList import views

app_name = 'todoList'

urlpatterns = [
    path('',      views.TodoListView.as_view(), name="home-todo"),
    path("lista/", views.TodoListView.as_view(), name="lista-todo"),
    path("cria/", views.TodoCreateView.as_view(), name="cria-todo"),
    path("atualiza/<int:pk>", views.TodoUpdateView.as_view(), name="atualiza-todo"),
    path("apaga/<int:pk>", views.TodoDeleteView.as_view(), name="apaga-todo"),
    path('minhasTarefas/', views.AuthorListView.as_view(), name="todo-minhasTarefas"),
]
