from django.shortcuts import render
from django.contrib.auth.models import User
from apps.redSocial.models import Perfil, AreaConocimiento, Interes, Multimedia, Canal, Post, Like, Comentario, Evento
from rest_framework import viewsets
from apps.redSocial.serializers import UserSerializer, AreaConocimientoSerializer, InteresSerializer, MultimediaSerializer, TimeLineSerializer, PerfilSerializer, EventoSerializer
from rest_framework.response import Response
import json
from django.core import serializers
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class AreaConocimientoViewSet(viewsets.ModelViewSet):
	queryset = AreaConocimiento.objects.all()
	serializer_class = AreaConocimientoSerializer
	
class InteresViewSet(viewsets.ModelViewSet):
	queryset = Interes.objects.all()
	serializer_class = InteresSerializer
	
class MultimediaViewSet(viewsets.ModelViewSet):
	queryset = Multimedia.objects.all()
	serializer_class = MultimediaSerializer

class TimeLineViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = TimeLineSerializer

	def list(self, request):
		posts = Post.objects.filter(usuario__perfil__areasConocimiento__descripcion__contains='Publico')
		#lista = [{'pk':post.pk, 'contenido':post.contenido} for post in posts]
		serializado = TimeLineSerializer(posts, many=True)
		#data = serializers.serialize('json', Post.objects.all())
		return Response(serializado.data)

class PerfilViewSet(viewsets.ModelViewSet):
	queryset = Perfil.objects.all()
	serializer_class = PerfilSerializer

class EventoViewSet(viewsets.ModelViewSet):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer
