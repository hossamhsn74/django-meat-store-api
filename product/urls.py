from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(), name='categorylist'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='categoryDetails'),
    path('product/', ProductListCreateView.as_view(), name='productlist'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='productDetails'),
    path('slider/', SliderImageView.as_view(), name='SliderImageView'),
    # path('product/<int:product_id>/buy', AddProductToCartView.as_view(), name='productDetails'),
    # path('cartitem/', CartItemListView.as_view()),
    # path('cartitem/<int:pk>/', CartItemDetailView.as_view()),
    # path('cart/', CartListCreateView.as_view()),
    # path('cart/<int:pk>/', CartDetailView.as_view(), name='categoryDetails'),
    path('order/', OrderListCreateView.as_view(), name='productlist'),
    path('order/<str:session_id>/', OrderDetailView.as_view(), name='productDetails'),

]
