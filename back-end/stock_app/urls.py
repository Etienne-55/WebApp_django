from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HelloWorld
from .views import signin, login, Hello
from .views import CoffeeViewSet

router = DefaultRouter()
router.register(r'coffee', CoffeeViewSet)

urlpatterns = [
    path('api/hello/', HelloWorld.as_view(), name='hello-world'),
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
    path('hello/', Hello.as_view(), name='hello'),
    path('api/', include(router.urls)),
]
