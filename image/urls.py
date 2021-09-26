from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *
router = SimpleRouter()
router.register('products', ProductModelViewSet, 'products')
router.register('avatars', AvatarModelViewSet, 'avatars')
router.register('categories', CategoryModelViewSet, 'categories')

urlpatterns = [
    path('', include(router.urls)),
]