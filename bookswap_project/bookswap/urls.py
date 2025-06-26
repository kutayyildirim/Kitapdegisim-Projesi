from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookswap.views.book_views import BookViewSet
from bookswap.views.user_views import UserViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
