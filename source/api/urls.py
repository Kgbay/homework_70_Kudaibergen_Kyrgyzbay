from django.urls import path

from api.views import TaskView, DetailView, UpdateView, DeleteView

urlpatterns = [
    path("tasks/", TaskView.as_view()),
    path("tasks/<int:pk>/", DetailView.as_view()),
    path("tasks/<int:pk>/update/", UpdateView.as_view()),
    path("tasks/<int:pk>/delete/", DeleteView.as_view()),
]
