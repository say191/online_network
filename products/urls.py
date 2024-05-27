from products.apps import ProductsConfig
from django.urls import path
import products.views as v

app_name = ProductsConfig.name

urlpatterns = [
    path('', v.ProductListAPIView.as_view(), name='products_list'),
    path('create/', v.ProductCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/', v.ProductRetrieveAPIView.as_view(), name='product_get'),
    path('update/<int:pk>/', v.ProductUpdateAPIView.as_view(), name='product_update'),
    path('delete/<int:pk>/', v.ProductDestroyAPIView.as_view(), name='product_delete'),
]
