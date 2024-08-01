from django.urls import path
from .views import ModelListView, ModelDetailView

urlpatterns = [
    path('', ModelListView.as_view(), name='model-list'),
    path('<int:pk>/', ModelDetailView.as_view(), name='model-detail'),
]
