from django.urls import path
from .views import HelloWorld
from .views import signin, login, Hello

urlpatterns = [
    path('api/hello/', HelloWorld.as_view(), name='hello-world'),
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
    path('hello/', Hello.as_view(), name='hello'),
]
