# REST Framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
# Permissions
from accounts.permissions import IsOwner
# Models
from accounts.models import EmergencyContact
# Serializers
from accounts.serializers import EmergencyContactSerializer

@permission_classes([IsAuthenticated,IsOwner])
class EmergencyContactRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Vista generica del modelo EmergencyContact, encargada de devolver y actualizar
    los datos del modelo. Permiso otorgado a usuarios autenticados y dueños de los datos.
    -
    Documentación de relevancia:
    * https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdateapiview
    * https://www.django-rest-framework.org/api-guide/permissions/#isauthenticated
    """
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer