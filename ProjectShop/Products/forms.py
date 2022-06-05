from django.forms import ModelForm, CharField
from Products.models import Products #type:ignore

class ProductForm(ModelForm):
    class Meta:
        model = Products

        fields = [
            "Id_category",
            "Product_name",
            "Price",
            "Image",
            "Describe",
            "Is_listed",
        ]

        title = CharField(min_length = 5, max_length = 256, required=True)

        # def clean(self):
        #     result = super().clean()
        #     logger.info(f"BookForm - clean run - result is {result}")
        #     return result

# class Basket(ModelForm):
#     class Meta:
#         model = Basket
#
#         fields = [
#             "Id_category",
#             "Product_name",
#             "Price",
#             "Image",
#             "Describe",
#             "Is_listed",
#         ]
