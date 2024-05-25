from django.urls import path
from . import views

urlpatterns = [
    path("", views.iris_home, name="iris_home"),
    path("predict/", views.iris_result, name="iris_result"),
    path("viewdata/", views.iris_dataset, name="iris_dataset"),
]
