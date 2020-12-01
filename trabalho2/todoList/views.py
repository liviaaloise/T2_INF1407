from django.shortcuts import render
from todoList.models import Tarefa
from todoList.forms import TarefaForm
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.

class TodoListView(View):
    def get(self,request,*args, **kwargs):
        todos = Tarefa.objects.all()
        context = {'todos': todos, }
        return render(request, 'todoList/listaTodo.html', context)

class TodoCreateView(View):
    def get(self,request,*args, **kwargs):
        context = {'formulario': TarefaForm, }
        return render(request, 'todoList/criaTodo.html', context)


    def post(self,request,*args, **kwargs):
        formulario = TarefaForm(request.POST)
        #formulario = dados do POST
        if formulario.is_valid():
            #contato somente em memoria
            print('formulario', formulario)
            todo = formulario.save()
            #salvar no banco
            todo.save()
            #redirecionar para outro view
            return HttpResponseRedirect(reverse_lazy('todoList:lista-todo'))
        else:
            return HttpResponseRedirect(reverse_lazy('todoList:cria-todo'))

class TodoUpdateView(View):

    def get(self,request,pk,*args, **kwargs):
        todo = Tarefa.objects.get(pk=pk)
        formulario = TarefaForm(instance=todo)
        context = {'todo': formulario, }
        return render(request, 'todoList/atualizaTodo.html', context)

    def post(self,request,pk,*args, **kwargs):
        todo = get_object_or_404(todo, pk=pk)
        formulario = TarefaForm(request.POST, instance=todo)

        if formulario.is_valid():
            todo = formulario.save()
            todo.save()
            return HttpResponseRedirect(reverse_lazy('todoList:lista-todo'))
        else:
            context = {'todo': formulario, }
            return render(request, 'todoList/atualizaTodo.html', context)


class TodoDeleteView(View):
    def get(self,request,pk,*args, **kwargs):
        todo = Tarefa.objects.get(pk=pk)
        context = {'todo': todo, }
        return render(request, 'todoList/apagaTodo.html',context)

    def post (self,request,pk,*args, **kwargs):
        todo = Tarefa.objects.get(pk=pk)
        todo.delete()
        print("Removendo o Todo", pk)
        return HttpResponseRedirect(reverse_lazy("todoList:lista-todo"))
