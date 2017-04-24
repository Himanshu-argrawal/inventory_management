from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView
from accounts.models import User
from .serializers import PostSerializer

class Postlistapiview(ListAPIView):
    queryset = User.objects.all()
    serializer_class = PostSerializer

class Postdetailapiview(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class =PostSerializer
    lookup_field = 'id'

class Postupdateapiview(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class =PostSerializer
    lookup_field = 'id'