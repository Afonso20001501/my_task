from typing import Any
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, DetailView
from .models import Task
from .forms import TaskForm
# Create your views here.


class Home(TemplateView):
      template_name = 'task/pages/index.html'

      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          task = Task.objects.filter(completed=True).order_by('-id')

          context.update({
               'task': task,
          })

          return context

class TaskView(DetailView):
     modal = Task
     template_name = 'task/pages/task_view.html'
     context_objects_name = 'task'

     def get_object(self, queryset=None):
          return get_object_or_404(Task, slug=self.kwargs.get('slug'), completed=True)
     
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["tasks_recentes"] = Task.objects.filter(completed=True).order_by('-id')
         return context

class NewTaskView(TemplateView):
     template_name = 'task/pages/new_task.html'

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          task = Task.objects.filter(completed=True).order_by('-id')

          context.update({
               'task': task,
               'task_form': TaskForm(),
          })

          return context
     
     def post(self, request, *args, **kwargs):
          task_form = TaskForm(request.POST)
          
          if task_form.is_valid():
               task_form.save()

          return self.get(request, *args, **kwargs)