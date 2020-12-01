from todoList.models import Tarefa
from django import forms

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
