from rest_framework import generics
from .models import *
from .serializers import *
from .integration.api_service import APIService
from django.conf import settings

# Initialize API service with base URL and token
api_service = APIService(base_url=settings.EBMS_BASE_URL, token=settings.EBMS_TOKEN)

class ModelListView(generics.ListCreateAPIView):
    queryset = <YourModel>.objects.all()
    serializer_class = ModelSerializer

    def get(self, request, *args, **kwargs):
        # Example API call
        data = api_service.get('endpoint')
        # Process and return the data as needed
        return Response(data)

    def post(self, request, *args, **kwargs):
        # Example API call
        data = api_service.post('endpoint', request.data)
        # Process and return the data as needed
        return Response(data)

class ModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = <YourModel>.objects.all()
    serializer_class = ModelSerializer

    def put(self, request, *args, **kwargs):
        # Example API call
        data = api_service.put(f'endpoints/{kwargs["pk"]}', request.data)
        # Process and return the data as needed
        return Response(data)

    def delete(self, request, *args, **kwargs):
        # Example API call
        api_service.delete(f'endpoints/{kwargs["pk"]}')
        return Response(status=status.HTTP_204_NO_CONTENT)
