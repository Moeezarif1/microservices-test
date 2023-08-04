from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
# Create your views here
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Product
# from .permissions import IsReadOnlyOrAuthenticated
from .serializers import ProductSerializer


class ProductAPI(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, pk, *args, **kwargs)

    @action(detail=True, methods=['GET'])
    def retrieve_product(self, request, pk=None):
        try:
            instance = Product.objects.get(product_id=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
