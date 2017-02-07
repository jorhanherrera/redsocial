from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class AreaConocimiento(models.Model):
	descripcion = models.CharField(max_length=25)
	estatus = models.CharField(max_length=1)

	def __str__(self):
		return '{}'.format(self.descripcion)

class Interes(models.Model):
	descripcion = models.CharField(max_length=25)
	estatus = models.CharField(max_length=1)

	def __str__(self):
		return '{}'.format(self.descripcion)

class Perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	fechaNacimiento = models.DateField()
	sexo = models.CharField(max_length=1)
	foto = models.ImageField()
	intereses = models.ManyToManyField(Interes)
	areasConocimiento = models.ManyToManyField(AreaConocimiento)

class Canal(models.Model):
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	areasConocimiento = models.ManyToManyField(AreaConocimiento)
	nombre = models.CharField(max_length=25)
	descripcion = models.TextField()
	fecha = models.DateTimeField()
	logo = models.ImageField()
	estatus = models.CharField(max_length=1)

class Evento(models.Model):
	titulo = models.CharField(max_length=25)
	descripcion = models.TextField()
	fecha = models.DateTimeField()
	logo = models.ImageField()
	propietario = models.ForeignKey(User, on_delete=models.CASCADE)
	estatus = models.CharField(max_length=1)

class Multimedia(models.Model):
	recurso = models.FileField()
	tipo = models.CharField(max_length=1)
	estatus = models.CharField(max_length=1)

class Post(models.Model):
	contenido = models.TextField()
	canal = models.ForeignKey(Canal,on_delete=models.CASCADE)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	multimedia = models.OneToOneField(Multimedia,on_delete=models.CASCADE)
	creado_en = models.DateTimeField(auto_now_add=True)
	estatus = models.CharField(max_length=1)

class Like(models.Model):
	propietario = models.ForeignKey(User,on_delete=models.CASCADE)
	post = models.ForeignKey(Post, editable=True, related_name='likes')
	fecha = models.DateTimeField(auto_now_add=True)
	estatus = models.CharField(max_length=1)

class Comentario(models.Model):
	propietario = models.ForeignKey(User,on_delete=models.CASCADE)
	post = models.ForeignKey(Post, editable=True, related_name='comentarios')
	mensaje = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)
	estatus = models.CharField(max_length=1)