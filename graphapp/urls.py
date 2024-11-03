from django.urls import path
from . import views

urlpatterns = [
    path('create-graph/', views.create_graph, name='create_graph'),
]
