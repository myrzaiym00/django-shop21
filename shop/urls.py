from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import CategoryViewSet, CommentViewSet, ProductViewSet, toggle_like, add_rating

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("comments", CommentViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('toggle_like/<int:p_id>/', toggle_like),
    path('add_rating/<int:p_id>/', add_rating),
]