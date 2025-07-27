from rest_framework import generics, mixins
from api.mixins import StaffEditorPermissionsMixin, UserQuerrySetMixin
from .models import Product
from .serializer import ProductSerializers



class ProductMixinsViews(generics.GenericAPIView,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)

    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)








class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers



class CreateProductView(UserQuerrySetMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.DjangoModelPermissions]
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffPermission]
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content, user=self.request.user)


    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     user = self.request.user
    #     return qs.filter(user=user)



class UpdateProductView(StaffEditorPermissionsMixin, UserQuerrySetMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    lookup_field = 'pk'
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)


class DeleteProductView(StaffEditorPermissionsMixin, UserQuerrySetMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'


class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


    def get_queryset(self):
        return super().get_queryset().filter(name__icontains='past')



























#@api_view(['POST'])
#def api_view(request):
    #query = Product.objects.all().order_by('?').first()
    #data = request.data
    #serializers = ProductSerializers(data=request.data)
    #if serializers.is_valid(raise_exception=True):
        #serializers.save()
        #return Response(serializers.data)
    #else:
        #return Response({'details':'invalid data'})

    #if query:
        #data = model_to_dict(query, fields=('name', 'content', 'price', 'get_discount'))
        #data = ProductSerializers(query).data
    #return Response(data)


