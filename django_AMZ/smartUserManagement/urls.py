from django.urls import path

from . import views

from django.contrib.auth.views import LoginView

app_name = 'sum'
urlpatterns = [
    path('', LoginView.as_view(template_name='admin/login.html'), name='login'),
]