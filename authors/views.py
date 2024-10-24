from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegisterForm

# Create your views here.
class AuthorView(TemplateView):
     template_name = 'authors/pages/register.html'

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)

          context.update({
               'register_form': RegisterForm(),
          })   

          return context  
     
     def post(self, request, *args, **kwargs):
          register_form = RegisterForm(request.POST)
          
          if register_form.is_valid():
                 register_form.save()
                 # Armazena os dados do formulário na sessão
                 request.session['register_form_data'] = register_form.cleaned_data
                    
                 # Você pode redirecionar ou retornar uma resposta apropriada aqui
                 return self.get(request, *args, **kwargs)

          else:
                raise Http404()
          
          return self.get(request, *args, **kwargs)