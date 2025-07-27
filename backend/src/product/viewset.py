from .models import Product
from .serializer import ProductSerializers
from rest_framework import mixins, viewsets



class ProductViewset(viewsets.ModelViewSet):
    """
    get -> list -> QuerySet
    get -> retrieve
    post -> create
    put -> update
    patch -> partial update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers





class ProductListRestrieveViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
