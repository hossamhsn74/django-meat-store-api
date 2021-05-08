from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class SliderImageView(generics.ListCreateAPIView):
    queryset = SliderImages.objects.all()
    serializer_class = SliderImagesSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        super(ProductDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        super(CategoryDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        if instance != None:
            serializer = self.get_serializer(instance)
            data = serializer.data

            products = Product.objects.filter(category=instance.id)
            serialized_products = ProductSerializer(products, many=True)
            data['products'] = serialized_products.data

            options = CategoryOptionValue.objects.filter(category=instance.id)
            serialized_options = CategoryOptionValueSerializer(
                options, many=True)
            data['options'] = serialized_options.data

            return Response(data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CartItemListView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def retrieve(self, request, *args, **kwargs):
        """ Get trip coordinates """
        super(CartItemDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        if instance != None:
            serializer = self.get_serializer(instance)
            data = serializer.data
            return Response(data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        super(CartItemDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

    def delete(self, request, *args, **kwargs):
        super(CartItemDetailView, self).delete(request, args, kwargs)
        return Response(status.HTTP_200_OK)


# class AddProductToCartView(APIView):

#     def post(self, request, product_id):
#         """
#         Return a list of all users.
#         """
#         print("session id", request.COOKIES)
#         get_product = get_object_or_404(Product, id=product_id)
#         if get_product != None:
#             quantity = request.POST.get('quantity')
#             notes = request.POST.get("notes")
#             beef_quantity = 0

#             price = get_product.price
#             total_item_price = int(quantity) * price
#             category = get_product.category

#             category_options = CategoryOptionValue.objects.filter(
#                 category=category)
#             variants_ids = []

#             cart_item = CartItem.objects.create(category=category, product=get_product, quantity=quantity,
#                                                 total_price=total_item_price, notes=notes, beef_quantity=beef_quantity)

#             for option in category_options:
#                 # option record = option.option_name
#                 # print("OPTION > ", str(option.option_name))
#                 print("Posted header >", request.POST.get(
#                     str(option.option_name.name)))

#                 for item in option.option_values.all():
#                     # value record = item
#                     print("Checking Value > ", item.value)

#                     if request.POST.get(str(option.option_name.name)) == item.value:
#                         print("passed value matched one of available values")
#                         single_variant = ProductVariant.objects.create(
#                             option_name=option.option_name, option_value=item)
#                         print('created variant with id', single_variant.id)
#                         variants_ids.append(single_variant)

#                         if option.option_name.name == "مفروم" and item.value == "نعم":
#                             beef_quantity = request.POST.get("beef_quantity")

#             if(len(variants_ids) == len(category_options)):
#                 cart_item.variants.add(*variants_ids)
#                 cart_item.alive_delivery_form = False
#             else:
#                 cart_item.variants.clear()
#                 cart_item.alive_delivery_form = True

#             response = CartItemSerializer(cart_item).data
#             return Response(response)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# class AddProductToCartView(request, id):
    # get_product = get_object_or_404(Product, id=id)
    # data = request.data
    # print("$$$$$$$$$$$$$$$$$$$4", data)
    # mycart_item = cart_item.objects.create(myproduct=get_product)
    # get_cart, created = cart.objects.get_or_create(user=user)
    # print(mycart_item)
    # print(get_cart.cart_items.all())

    # x = get_cart.cart_items.filter(myproduct=mycart_item.myproduct)
    # # if mycart_item not in get_cart.cart_items.all():
    # if not x.exists():
    #     get_cart.cart_items.add(mycart_item)
    # total = 0
    # for item in get_cart.cart_items.all():
    #     item.total = item.myproduct.price * item.number
    #     item.save()
    #     total += item.myproduct.price * item.number

    # get_cart.total = total
    # get_cart.save()
    # return HttpResponseRedirect(reverse("home"))


# def display_cart(request):
#     get_cart = get_object_or_404(cart, user=request.user)
#     return render(request, "cart.html", {'cart': get_cart})


# def remove_from_cart(request, id):
#     user = request.user
#     mycart = cart.objects.get(user=user)
#     mycart_item = get_object_or_404(cart_item, id=id)
#     mycart.cart_items.remove(mycart_item)
#     # mycart.total-=mycart_item.product.price
#     mycart.total -= mycart_item.total
#     mycart.save()
#     return HttpResponseRedirect(reverse('cart:display_cart'))


# def update_number(request, id):
#     mycart_item = get_object_or_404(cart_item, id=id)
#     mycart_item.number = request.POST['number']
#     mycart_item.save()
#     mycart = get_object_or_404(cart, user=request.user)
#     total = 0
#     for item in mycart.cart_items.all():
#         item.total = item.myproduct.price * item.number
#         item.save()
#         total += item.myproduct.price * item.number
#     mycart.total = total
#     mycart.save()

#     print(mycart_item.number)
#     print(id)
#     print(request.POST['number'])
#     return HttpResponseRedirect(reverse('cart:display_cart'))


class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        super(CartDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "result": data}
        return Response(response)


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        customer_name = self.request.data['name']
        session_id = self.request.data['session_id']
        customer_address = self.request.data['address']
        customer_phone = self.request.data['phone']
        customer_payment_method = self.request.data['payment_method']
        order_confirmation_method = self.request.data['order_confirmation_method']
        
        if customer_payment_method == None:
            customer_payment_method = "cash_on_delivery"
        # cart
        cart = self.request.data['cart']
        if cart != None:
            items = cart['item']
            # cart items
            cart_items = []
            if items:
                for item in items:
                    # single cart item
                    # print("ITEM : ", item)
                    quantity = item['quantity']
                    if quantity == 0:
                        quantity = 1
                    notes = item['notes']
                    alive_delivery_form = item['beef_quantity']
                    beef_quantity = item['beef_quantity']
                    fridge_status = item['fridge_status']

                    # get product info
                    # query can be based on (name or ID)()
                    print("##########3", item["product"])
                    product_input = item['product']
                    get_product = get_object_or_404(
                        Product, id=product_input['id'])
                    if get_product != None:
                        price = get_product.price
                        total_item_price = int(quantity) * price

                    cart_item = CartItem.objects.create(category=get_product.category, product=get_product, quantity=quantity,
                                                        total_price=total_item_price, notes=notes, fridge_status=fridge_status, beef_quantity=beef_quantity)

                    # category_options = CategoryOptionValue.objects.filter(
                    #     category=get_product.category)

                    variants_ids = []
                    variants = item['variants']
                    if variants:
                        alive_delivery_form = False
                        for variant in variants:
                            # key , value

                            # query for key by name
                            # query for value by value
                            variant_name_input = variant['option_name']['name']
                            variant_name = Option.objects.get(
                                name=variant_name_input)
                            variant_value_input = variant['option_value']['value']
                            variant_value = Value.objects.get(
                                value=variant_value_input)

                            # if variant_name == "مفروم" and variant_value == "نعم":
                            #     beef_quantity = item['beef_quantity']
                            #     cart_item.beef_quantity = beef_quantity
                            #     cart_items.save()

                            # create productVariant record
                            single_variant = ProductVariant.objects.create(
                                option_name=variant_name, option_value=variant_value)
                            # add to cart item variants
                            variants_ids.append(single_variant)

                    if(len(variants_ids)):
                        cart_item.variants.add(*variants_ids)
                        cart_item.alive_delivery_form = False
                    else:
                        cart_item.variants.clear()
                        cart_item.alive_delivery_form = True

                    cart_item.save()
                    cart_items.append(cart_item)

            # handle cart total amount
            total_cart_amount = 0
            for item in cart_items:
                total_cart_amount += item.total_price

            if cart_items:
                order_cart = Cart.objects.create(
                    total_amount=total_cart_amount)
                order_cart.item.add(*cart_items)
                order_cart.save()

                order = Order.objects.create(name=customer_name, address=customer_address, session_id=session_id,
                                             phone=customer_phone, payment_method=customer_payment_method, cart=order_cart, order_confirmation_method=order_confirmation_method)
                order.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response("invalid request, empty cart")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response("order created", status=status.HTTP_201_CREATED)


class OrderDetailView(views.APIView):
    """
    Get all orders for specific session_id
    """

    def get_object(self, session_id):
        try:
            return Order.objects.filter(session_id=session_id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, session_id, format=None):
        orders = self.get_object(session_id)
        print("orders", orders)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
