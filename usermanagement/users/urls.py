from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostAndGetHandler.as_view(), name='add-and-get-users'),
    path('<str:id>', views.GetPutDeleteHandler.as_view(), name='get-put-delete-user'),
]
