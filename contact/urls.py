from django.urls import path
from .views import NewSerializer, NewContact, NewDetailContactAPIView

urlpatterns = [
    path('contact/', NewContact.as_view()),
    path('contact/<int:pk>/',NewDetailContactAPIView.as_view()),
]
