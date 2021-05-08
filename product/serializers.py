from rest_framework import serializers

from .models import *


class OptionNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ('name',)
        # fields = "__all__"


class SliderImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    
    class Meta:
        model = SliderImages
        fields = "__all__"


class OptionValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Value
        # fields = "__all__"
        fields = ('value',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class VariantSerializer(serializers.ModelSerializer):
    option_name = OptionNameSerializer(read_only=True)
    option_value = OptionValueSerializer(read_only=True)

    class Meta:
        model = ProductVariant
        fields = ('option_name', 'option_value',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=False)
    variants = VariantSerializer(many=True, read_only=False)

    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ('category',)


class CartSerializer(serializers.ModelSerializer):
    item = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('name',)


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ('value',)


class CategoryOptionValueSerializer(serializers.ModelSerializer):
    option_name = OptionSerializer(many=False, read_only=True)
    option_values = ValueSerializer(many=True, read_only=True)

    class Meta:
        model = CategoryOptionValue
        fields = ('option_name', 'option_values')


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = '__all__'
