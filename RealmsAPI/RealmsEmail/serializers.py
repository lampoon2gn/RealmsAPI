from .models import ClientMsg
from rest_framework import serializers

class ClientMsgSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ClientMsg
    fields =  ('id','name','email','message','date_posted')
