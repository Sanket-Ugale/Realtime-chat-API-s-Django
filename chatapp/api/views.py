# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from api.models import GrpMsg
from api.serializers import GrpMsgSerializer

class GrpMsgCreateView(generics.CreateAPIView):
    queryset = GrpMsg.objects.all()
    serializer_class = GrpMsgSerializer

class GrpMsgUpdateView(generics.UpdateAPIView):
    queryset = GrpMsg.objects.all()
    serializer_class = GrpMsgSerializer

class GrpMsgDeleteView(generics.DestroyAPIView):
    queryset = GrpMsg.objects.all()
    serializer_class = GrpMsgSerializer
