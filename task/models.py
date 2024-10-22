from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    categoria = models.CharField(max_length=200, verbose_name='Categoria')
    class Meta:
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.categoria

DEPARTAMENTO = (
    (0,"Gestão_Arquivo"),
    (1,"Processamento_Salário"),
    (2,"Organização_Agenda"),
    (3,"Controle_Inventário"),
   
)


class Task(models.Model):
      title = models.CharField(max_length=200)
      description = models.TextField()
      completed = models.BooleanField(default=False)
      slug = models.SlugField(unique=True)
      time_completed = models.DateTimeField(auto_now_add=True)    
      author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
      )
      category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
      )

      def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

      class Meta:
        verbose_name_plural = 'Tasks'
      def __str__(self):
            return self.title
