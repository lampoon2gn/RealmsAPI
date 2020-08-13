from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientMsgSerializer
from .models import ClientMsg
# Create your views here.

class ClientMsgViewSet(viewsets.ModelViewSet):
  queryset = ClientMsg.objects.all().order_by('date_posted')
  serializer_class = ClientMsgSerializer