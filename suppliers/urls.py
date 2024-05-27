from suppliers.apps import SuppliersConfig
from django.urls import path
import suppliers.views as v

app_name = SuppliersConfig.name

urlpatterns = [
    path('', v.SupplierListAPIView.as_view(), name='users_list'),
    path('create/', v.SupplierCreateAPIView.as_view(), name='user_create'),
    path('<int:pk>/', v.SupplierRetrieveAPIView.as_view(), name='user_get'),
    path('update/<int:pk>/', v.SupplierUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', v.SupplierDestroyAPIView.as_view(), name='user_delete')
]
