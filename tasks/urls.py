from django.urls import path
from .views import IndexView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="list"),
    path("update_task/<str:pk>/", TaskUpdateView.as_view(), name="update_task"),
    path("delete_task/<str:pk>/", TaskDeleteView.as_view(), name="delete"),
]
