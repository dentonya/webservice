from .views import OrderViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'order',OrderViewSet,basename="order")

urlpatterns = [
    path("",include(router.urls))
]
