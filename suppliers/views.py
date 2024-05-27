from rest_framework.viewsets import generics
from suppliers.serializers import SupplierSerializer
from suppliers.models import Supplier
from users.permissions import IsCreatorForSupplier
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class SupplierCreateAPIView(generics.CreateAPIView):
    """View for creating supplier"""
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        supplier = serializer.save()
        supplier.author = self.request.user
        if supplier.type == 'FA':
            supplier.level = 0
        if supplier.type in ['RN', 'IE']:
            if supplier.supplier:
                if supplier.supplier.level == 0:
                    supplier.level = 1
                else:
                    supplier.level = 2
            else:
                supplier.level = 0
        supplier.save()


class SupplierListAPIView(generics.ListAPIView):
    """View for displaying all suppliers"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    permission_classes = [IsAuthenticated, ]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """View for displaying one chosen supplier"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated, ]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """View for supplier updating"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsCreatorForSupplier | IsAdminUser, ]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """View for deleting one chosen supplier"""
    queryset = Supplier.objects.all()
    permission_classes = [IsCreatorForSupplier | IsAdminUser, ]
