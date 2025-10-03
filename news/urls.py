from django.urls import path
from .views import NewSerializer, NewListCreateAPIView, NewDetailCreateAPIView

urlpatterns = [
    path('news/', NewListCreateAPIView.as_view()),
    path('news/<int:pk>/',NewDetailCreateAPIView.as_view()),
]
