from django.urls import path
from .views import ListTask, Detail

urlpatterns = [
    path('list/', ListTask.as_view()),
    path('list/<int:task_id>/', Detail.as_view())
]
