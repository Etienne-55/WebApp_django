from django.urls import path
from .views import HelloWorld, Get_name, Get_password, Get_Email

urlpatterns = [
    path('api/hello/', HelloWorld.as_view(), name='hello-world'),
    path('api/hello/', Get_name.as_view(), name='get-name'),
    path('api/hello/', Get_password.as_view(), name='get-password'),
    path('api/hello_again/', Get_Email.as_view(), name='get-email')
]
