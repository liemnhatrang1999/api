

from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from crudapi.views import ProductViewSet


router = DefaultRouter()
router.register('api',ProductViewSet)

urlpatterns=[
    path('',include(router.urls))

]