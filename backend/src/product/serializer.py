from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validators_unique_product_name, validate_product_name
from api.serializer import UserPublicSerializer



# class UserProductInlineSerializer(serializers.Serializer):
#     url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
#     email = serializers.EmailField(write_only=True)
#     name = serializers.CharField()

class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # owner = serializers.SerializerMethodField(read_only=True)
    # owner = UserProductInlineSerializer(source='user.product_set.all', many=True, read_only=True)
    owner = UserPublicSerializer(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validators_unique_product_name])
    # user_name = serializers.CharField(source="user.username", read_only=True) #ne pas utuliser


    class Meta:
        model = Product
        fields = ('pk', 'name', 'content', 'price', 'my_discount', 'url', 'email', 'owner')


    def create(self, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        print(email)
        print(validated_data)
        #return Product.objects.create(**validated_data)
        obj = super().create(validated_data)
        return obj

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        return super().update(instance, validated_data)


    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-detail", kwargs={'pk':obj.pk}, request=request)

    # def get_owner(self, obj):
    #     return {'username': obj.user.username, 'id':obj.user.pk}

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount
