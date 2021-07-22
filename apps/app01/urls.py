from django.urls import path
from . import views

app_name = 'app01'


urlpatterns = [
    path('',views.test_celery)
]
