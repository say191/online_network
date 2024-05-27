from rest_framework.viewsets import generics
from products.serializers import ProductSerializer
from products.models import Product
from users.permissions import IsCreatorForProduct
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ProductCreateAPIView(generics.CreateAPIView):
    """View for creating product"""
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        product = serializer.save()
        product.author = self.request.user
        product.save()


class ProductListAPIView(generics.ListAPIView):
    """View for displaying all products"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, ]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """View for displaying one chosen product"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, ]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """View for product updating"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsCreatorForProduct | IsAdminUser, ]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """View for deleting one chosen product"""
    queryset = Product.objects.all()
    permission_classes = [IsCreatorForProduct | IsAdminUser, ]
