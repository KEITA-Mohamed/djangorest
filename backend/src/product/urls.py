from django.urls import path

from .views import DetailProductView, CreateProductView, UpdateProductView, DeleteProductView, ListProductView, ProductMixinsViews

urlpatterns = [
    path('<int:pk>/', DetailProductView.as_view(), name='product-detail'),
    path('create/', CreateProductView.as_view()),
    path('<int:pk>/update', UpdateProductView.as_view(), name='product-update'),
    path('<int:pk>/delete', DeleteProductView.as_view()),
    path('list/', ListProductView.as_view()),
    # path('create/', ProductMixinsViews.as_view()),
    # path('<int:pk>/detail', ProductMixinsViews.as_view(), name='product-detail'),
    # path('<int:pk>/update', ProductMixinsViews.as_view(), name='product-update'),
    # path('<int:pk>/delete', ProductMixinsViews.as_view()),
    # path('list/', ProductMixinsViews.as_view()),

]