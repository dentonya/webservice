from .views import CustomerViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'customer',CustomerViewSet,basename="customer")

urlpatterns = [
    path("",include(router.urls))
]
