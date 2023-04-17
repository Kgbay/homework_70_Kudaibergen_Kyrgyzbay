from django.urls import path

from api.views import TaskView

urlpatterns = [
    path("tasks/", TaskView.as_view(), name='tasks'),
]
