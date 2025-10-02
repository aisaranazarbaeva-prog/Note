from django.urls import path
from .views import (
    GetNotesAPIView,
    GetNoteByIdAPIView,
    CreateNoteAPIView,
    UpdateNoteAPIView,
    DeleteNoteAPIView
)

urlpatterns = [
    path('notes/', GetNotesAPIView.as_view(), name='note-list'),
    path('notes/', CreateNoteAPIView.as_view(), name='note-create'),
    path('notes/<int:pk>/', GetNoteByIdAPIView.as_view(), name='note-detail'),
    path('notes/<int:pk>/', UpdateNoteAPIView.as_view(), name='note-update'),
    path('notes/<int:pk>/', DeleteNoteAPIView.as_view(), name='note-delete'),
]
