from rest_framework.viewsets import ReadOnlyModelViewSet

from products.models import Product
from .serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.filter(
            productuser__owner=user,
            productuser__access=True
            )
        return queryset
