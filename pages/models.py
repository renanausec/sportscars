from django.db import models


# Create your models here.

class Equipe(models.Model):
    primeiro_nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='fotos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.primeiro_nome