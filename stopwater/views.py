from stopwater.models import Registro
from stopwater.serializers import RegistroSerializer
from rest_framework import viewsets

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
