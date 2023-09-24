from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Count, Q, Sum, FloatField, ExpressionWrapper, F

from products.models import Product
from .serializers import ProductSerializer

User = get_user_model()


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.filter(product_user__owner=user).prefetch_related('lessons__user_lesson')
        return queryset

    @action(detail=False)
    def get_statistics(self, request):
        total_users = User.objects.all().count()

        products = Product.objects.annotate(
            total_viewed_lessons=Count('lessons__user_lesson', filter=Q(lessons__user_lesson__is_viewed=True), distinct=True),
            total_viewed_time=Sum('lessons__user_lesson__viewed_time', distinct=True),
            total_students=Count('product_user__owner', distinct=True),
            owners_percentage=ExpressionWrapper(
                F('total_students') * 100.0 / total_users,
                output_field=FloatField()
            )
        )

        product_statistics = []

        for product in products:
            product_statistics.append({
                'product_name': product.name,
                'total_views': product.total_viewed_lessons,
                'total_viewed_time': product.total_viewed_time,
                'owners_number': product.total_students,
                'students_percentage': product.owners_percentage
            })

        return Response(product_statistics)
